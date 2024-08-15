from django.db import models
import uuid
from api.models import rubrica_estado, beneficiario, actividade, fornecedor, moeda, sub_rubrica, rubrica_projecto


class EstadoPagamento(models.TextChoices):
    PENDENTE = 'PENDENTE'
    PAGA = 'PAGA'
    ACTIVA = 'ACTIVA'


class Requisicao(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nr_requisicao_interna = models.CharField(max_length=255)
    nome_documento = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    rubrica_estado = models.ForeignKey(rubrica_estado.RubricaEstado, on_delete=models.PROTECT,
                                       related_name='requisicao_rubrica_estado', null=True)
    moeda_requisicao = models.ForeignKey(moeda.Moeda, on_delete=models.PROTECT, related_name='moeda_requisicao', null=True)
    irps = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    fornecedor = models.ForeignKey(fornecedor.Fornecedor, on_delete=models.PROTECT,
                                   related_name='fornecedor_requisicao', null=True)
    beneficiario = models.ForeignKey(beneficiario.Beneficiario, on_delete=models.PROTECT,
                                     related_name='beneficiario_requisicao', null=True)
    actividade = models.ForeignKey(actividade.Actividade, on_delete=models.PROTECT,
                                   related_name='actividade_requisicao', null=True)
    rubrica_projecto = models.ForeignKey(rubrica_projecto.RubricaProjecto, on_delete=models.PROTECT,
                                         related_name='rubrica_projecto_requisicao', null=True)
    sub_rubrica = models.ForeignKey(sub_rubrica.SubRubrica, on_delete=models.PROTECT,
                                    related_name='sub_rubrica_requisicao', null=True)
    nr_referencia = models.IntegerField()
    nr_documento = models.IntegerField()
    data_emissao = models.DateField()
    valor = models.DecimalField(max_digits=20, decimal_places=3)
    valor_total = models.DecimalField(max_digits=20, decimal_places=3)
    estado_pagamento = models.CharField(max_length=255, choices=EstadoPagamento, default=EstadoPagamento.ACTIVA)
    # calcular no front
    valor_moeda_distribuicao = models.DecimalField(max_digits=20, decimal_places=3, null=True)
    # associar no front
    moeda_distribuicao = models.ForeignKey(moeda.Moeda, on_delete=models.PROTECT, related_name='moeda_distribuicao', null=True)
    # distribuicao = models.ForeignKey(distribuicao.Distribuicao, on_delete=models.PROTECT, related_name='distribuicao_requisicao')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descricao
