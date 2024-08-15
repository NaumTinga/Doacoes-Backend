from django.db import models
from api.models import coordenador, financiamento, moeda
import uuid
from django.core.exceptions import ValidationError
from django.db import transaction
from django.utils.translation import gettext_lazy as _


class Projecto(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=50, decimal_places=3)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    financiamento = models.ForeignKey(financiamento.Financiamento, on_delete=models.PROTECT,
                                      related_name='financiamento')
    moeda_projecto = models.ForeignKey(moeda.Moeda, on_delete=models.PROTECT, related_name='moeda_projecto',
                                        null=True)
    coordenador = models.ForeignKey(coordenador.Coordenador, on_delete=models.PROTECT, related_name='coordenador')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    def clean(self):
        super().clean()
        if self.valor > self.financiamento.valor:
            raise ValidationError(_('Valor do Projecto não pode ser maior que o valor do Financiamento.'))

        if self.data_inicio < self.financiamento.data_inicio or self.data_fim > self.financiamento.data_fim:
            raise ValidationError(_('As datas do Projecto devem estar dentro do período das datas do Financiamento.'))

    def save(self, *args, **kwargs):
        self.clean()

        # Set moeda_projecto to the same as moeda_financiamento if not provided
        if not self.moeda_projecto:
            self.moeda_projecto = self.financiamento.moeda_financiador

        with transaction.atomic():
            financiamento = self.financiamento

            if self.pk is not None:
                # Update scenario: adjust the financiamento valor based on the difference
                original_projecto = Projecto.objects.get(pk=self.pk)
                valor_difference = self.valor - original_projecto.valor
                financiamento.valor -= valor_difference
            else:
                # Create scenario: subtract the subprojecto valor from the projecto
                financiamento.valor -= self.valor

            if financiamento.valor < 0:
                raise ValidationError(_('Financiamento value cannot be negative.'))

            financiamento.save()
            super().save(*args, **kwargs)

    def save_without_validation(self, *args, **kwargs):
        with transaction.atomic():
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        with transaction.atomic():
            financiamento = self.financiamento
            financiamento.valor += self.valor
            financiamento.save()
            super().delete(*args, **kwargs)
