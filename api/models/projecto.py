from django.db import models
from api.models import coordenador, financiamento
import uuid
from django.core.exceptions import ValidationError
from django.db import transaction
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=50, decimal_places=3)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    financiamento = models.ForeignKey(financiamento.Financiamento, on_delete=models.PROTECT,
                                      related_name='financiamento')
    coordenador = models.ForeignKey(coordenador.Coordenador, on_delete=models.PROTECT, related_name='coordenador')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    def clean(self):
        super().clean()
        if self.valor > self.financiamento.valor:
            raise ValidationError(_('Project value cannot be greater than the financing value.'))

        if self.data_inicio < self.financiamento.data_inicio or self.data_fim > self.financiamento.data_fim:
            raise ValidationError(_('Project dates must be within the financing period.'))

    # def save(self, *args, **kwargs):
    #     self.clean()
    #     return super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.clean()
        with transaction.atomic():
            # Lock the financiamento row to prevent race conditions
            financiamento = self.financiamento
            financiamento.valor -= self.valor
            if financiamento.valor < 0:
                raise ValidationError(_('Financiamento value cannot be negative.'))
            financiamento.save()
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        with transaction.atomic():
            financiamento = self.financiamento
            financiamento.valor += self.valor
            financiamento.save()
            super().delete(*args, **kwargs)