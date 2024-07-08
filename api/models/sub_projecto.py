from django.db import models
import uuid
from api.models import projecto, actividade, beneficiario
from django.core.exceptions import ValidationError
from django.db import transaction
from django.utils.translation import gettext_lazy as _


class SubProjecto(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    projecto = models.ForeignKey(projecto.Projecto, on_delete=models.PROTECT, related_name='subprojectos')
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=20, decimal_places=3)
    actividade = models.ForeignKey(actividade.Actividade, on_delete=models.PROTECT, related_name='actividade', null=True)
    beneficiario = models.ForeignKey(beneficiario.Beneficiario, on_delete=models.PROTECT, related_name='beneficiario', null=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descricao

    def clean(self):
        super().clean()
        if self.valor > self.projecto.valor:
            raise ValidationError(_('Valor do SubProjecto não pode ser maior que o valor do Projecto.'))

        if self.data_inicio < self.projecto.data_inicio or self.data_fim > self.projecto.data_fim:
            raise ValidationError(_('As datas do SubProjecto devem estar dentro do período das datas do Projecto.'))

    def save(self, *args, **kwargs):
        self.clean()
        with transaction.atomic():
            projecto = self.projecto

            if self.pk is not None:
                # Update scenario: adjust the projecto valor based on the difference
                original_subprojecto = SubProjecto.objects.get(pk=self.pk)
                valor_difference = (self.valor or 0) - (original_subprojecto.valor or 0)
                projecto.valor -= valor_difference
            else:
                # Create scenario: subtract the subprojecto valor from the projecto
                projecto.valor -= (self.valor or 0)

            if projecto.valor < 0:
                raise ValidationError(_('Projecto value cannot be negative.'))

            projecto.save_without_validation()
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        with transaction.atomic():
            projecto = self.projecto
            projecto.valor += (self.valor or 0)
            projecto.save_without_validation()
            super().delete(*args, **kwargs)
