from django.db import models, transaction
import uuid
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from api.models import rubrica_estado, fornecedor, moeda, sub_rubrica, rubrica_projecto
from api.models.cambio import Cambio


class EstadoPagamento(models.TextChoices):
    PENDENTE = 'PENDENTE'
    PAGA = 'PAGA'
    ACTIVA = 'ACTIVA'


class RequisicaoRubrica(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nr_requisicao_interna = models.CharField(max_length=255)
    nome_documento = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    rubrica_estado = models.ForeignKey(rubrica_estado.RubricaEstado, on_delete=models.PROTECT,
                                       related_name='rubrica_estado_requisicao', null=True)
    moeda_requisicao = models.ForeignKey(moeda.Moeda, on_delete=models.PROTECT, related_name='requisicao_moeda',
                                         null=True)
    irps = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    fornecedor = models.ForeignKey(fornecedor.Fornecedor, on_delete=models.PROTECT,
                                   related_name='requisicao_fornecedor', null=True)
    rubrica_projecto = models.ForeignKey(rubrica_projecto.RubricaProjecto, on_delete=models.PROTECT,
                                         related_name='requisicao_rubrica_projecto', null=True)
    sub_rubrica = models.ForeignKey(sub_rubrica.SubRubrica, on_delete=models.PROTECT,
                                    related_name='requisicao_sub_rubrica', null=True)
    nr_referencia = models.IntegerField()
    nr_documento = models.IntegerField()
    data_emissao = models.DateField()
    valor_inicial = models.DecimalField(max_digits=20, decimal_places=3)
    valor_convertido = models.DecimalField(max_digits=20, decimal_places=3, null=True)
    estado_pagamento = models.CharField(max_length=255, choices=EstadoPagamento, default=EstadoPagamento.PENDENTE)
    valor_moeda_distribuicao = models.DecimalField(max_digits=20, decimal_places=3, null=True)
    moeda_distribuicao = models.ForeignKey(moeda.Moeda, on_delete=models.PROTECT,
                                           related_name='moeda_distribuicao_requisicao', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descricao

    def clean(self):
        super().clean()
        if self.sub_rubrica and self.valor_convertido is not None:
            if self.valor_convertido > self.sub_rubrica.valor:
                raise ValidationError(_('Valor total não pode ser maior que o valor da Sub Rubrica'))

    def save(self, *args, **kwargs):
        self.clean()

        # Perform currency conversion if necessary
        if self.moeda_requisicao and self.moeda_distribuicao and self.moeda_requisicao != self.moeda_distribuicao:
            exchange_rate = Cambio.get_exchange_rate(self.moeda_distribuicao, self.moeda_requisicao)
            self.valor_convertido = self.valor_inicial * exchange_rate

        if self.valor_convertido is None:
            self.valor_convertido = self.valor_inicial  # Default to valor_inicial if no conversion is needed

        with transaction.atomic():
            if self.pk is not None:
                original_requisicao = RequisicaoRubrica.objects.get(pk=self.pk)
                valor_difference = self.valor_convertido - (original_requisicao.valor_convertido or 0)
                self.sub_rubrica.valor -= valor_difference
            else:
                self.sub_rubrica.valor -= self.valor_convertido

            if self.sub_rubrica.valor < 0:
                raise ValidationError(_('Valor da Sub Rubrica não pode ser negativa'))

            self.sub_rubrica.save_without_validation()
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        with transaction.atomic():
            self.sub_rubrica.valor += self.valor_convertido or 0
            self.sub_rubrica.save()
            super().delete(*args, **kwargs)