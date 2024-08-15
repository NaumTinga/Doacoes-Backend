from django.db import models, transaction
import uuid
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from api.models import rubrica_projecto, moeda


class SubRubrica(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    codigo_rubrica = models.CharField(max_length=55)
    nome = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=20, decimal_places=3, null=True)
    rubrica_projecto = models.ForeignKey(rubrica_projecto.RubricaProjecto, on_delete=models.PROTECT,
                                         related_name='sub_rubrica')
    moeda_sub_rubrica = models.ForeignKey(moeda.Moeda, on_delete=models.PROTECT, related_name='moeda_sub_rubrica',
                                          null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    def clean(self):
        super().clean()
        if self.valor is not None and self.rubrica_projecto.valor is not None:
            if self.valor > self.rubrica_projecto.valor:
                raise ValidationError(_('Valor da Sub Rubrica não pode ser maior que o valor da Rubrica Projecto'))
        elif self.valor is not None and self.rubrica_projecto.valor is None:
            raise ValidationError(_('Valor da Rubrica Projecto não pode ser nulo'))

    def save(self, *args, **kwargs):
        self.clean()

        # Set moeda_projecto to the same as moeda_rubricaProjecto if not provided
        if not self.moeda_sub_rubrica:
            self.moeda_sub_rubrica = self.rubrica_projecto.moeda_rubrica

        with transaction.atomic():
            rubrica_projecto = self.rubrica_projecto

            if self.pk is not None:
                # Update to adjust the value based on the difference
                original_rubrica = SubRubrica.objects.get(pk=self.pk)
                valor_difference = self.valor - (original_rubrica.valor or 0)
                rubrica_projecto.valor -= valor_difference
            else:
                rubrica_projecto.valor -= (self.valor or 0)

            if rubrica_projecto.valor < 0:
                raise ValidationError(_('Rubrica Projecto nao pode ser negativa'))

            rubrica_projecto.save_without_validation()
            super().save(*args, **kwargs)

    def save_without_validation(self, *args, **kwargs):
        with transaction.atomic():
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        with transaction.atomic():
            rubrica_projecto = self.rubrica_projecto
            rubrica_projecto.valor += (self.valor or 0)
            rubrica_projecto.save_without_validation()
            super().delete(*args, **kwargs)
