from django.db import models
import uuid
from api.models import projecto, moeda
from django.core.exceptions import ValidationError
from django.db import transaction
from django.utils.translation import gettext_lazy as _


class RubricaProjecto(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    codigo_rubrica = models.CharField(max_length=55)
    nome = models.CharField(max_length=55)
    valor = models.DecimalField(max_digits=20, decimal_places=3, null=True)
    projecto = models.ForeignKey(projecto.Projecto, on_delete=models.PROTECT, related_name='rubrica_projectos')
    moeda_rubrica = models.ForeignKey(moeda.Moeda, on_delete=models.PROTECT, related_name='moeda_rubrica',
                                      null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    def clean(self):
        super().clean()
        if self.valor is not None and self.valor > self.projecto.valor:
            raise ValidationError(_('Valor da RubricaProjecto não pode ser maior que o valor do Projecto.'))

    def save(self, *args, **kwargs):
        self.clean()

        # Set moeda_projecto to the same as moeda_projecto if not provided
        if not self.moeda_rubrica:
            self.moeda_rubrica = self.projecto.moeda_projecto

        with transaction.atomic():
            projecto = self.projecto

            if self.pk is not None:
                # Update scenario: adjust the projecto valor based on the difference
                original_rubrica = RubricaProjecto.objects.get(pk=self.pk)
                valor_difference = self.valor - (original_rubrica.valor or 0)
                projecto.valor -= valor_difference
            else:
                # Create scenario: subtract the rubrica valor from the projecto
                projecto.valor -= (self.valor or 0)

            if projecto.valor < 0:
                raise ValidationError(_('Projecto value cannot be negative.'))

            projecto.save_without_validation()
            super().save(*args, **kwargs)

    def save_without_validation(self, *args, **kwargs):
        with transaction.atomic():
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        with transaction.atomic():
            projecto = self.projecto
            projecto.valor += (self.valor or 0)
            projecto.save_without_validation()
            super().delete(*args, **kwargs)
