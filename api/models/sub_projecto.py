from django.db import models
import uuid
from api.models import projecto, actividade, beneficiario
from django.core.exceptions import ValidationError
from django.db import transaction
from django.utils.translation import gettext_lazy as _


class SubProjecto(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    projecto = models.ForeignKey(projecto.Projecto, on_delete=models.PROTECT, related_name='projecto')
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=20, decimal_places=3)
    activade = models.ForeignKey(actividade.Actividade, on_delete=models.PROTECT, related_name='actividade', null=True)
    beneficiario = models.ForeignKey(beneficiario.Beneficiario, on_delete=models.PROTECT, related_name='beneficiario', null=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descricao

        # Este metodo verifica se o valor e as datas sao iguais ou inferiores as do financiamento
        # Data inicio e fim devem ser iguais ou inferiores ao financiamento, o valor tambem deve ser igual ou superior
    def clean(self):
        super().clean()
        if self.valor > self.projecto.valor:
            raise ValidationError(_('Valor do SubProjecto não pode ser maior que o valor do Projecto.'))

        if self.data_inicio < self.projecto.data_inicio and self.data_fim > self.projecto.data_fim:
            raise ValidationError(_('As datas do SubProjecto devem estar dentro do período das datas do Projecto.'))

    # Cria o subprojecto e faz update, tendo em conta o valor do projecto
    # subtrai e adiciona os valores do projecto associado ao subprojecto
    def save(self, *args, **kwargs):
        self.clean()
        with transaction.atomic():
            projecto = self.projecto

            if self.pk is not None:
                # Update scenario: adjust the projecto valor based on the difference
                original_subprojecto = SubProjecto.objects.get(pk=self.pk)
                valor_difference = self.valor - original_subprojecto.valor
                projecto.valor -= valor_difference
            else:
                # Create scenario: subtract the subprojecto valor from the projecto
                projecto.valor -= self.valor

            if projecto.valor < 0:
                raise ValidationError(_('Projecto value cannot be negative.'))

            projecto.save()
            super().save(*args, **kwargs)
            self._original_valor = self.valor  # Update the original valor after saving

    # # Subtrair o valor do financiamento
    # def save(self, *args, **kwargs):
    #     self.clean()
    #     with transaction.atomic():
    #         # Lock the projecto row to prevent race conditions
    #         projecto = self.projecto
    #         projecto.valor -= self.valor
    #         if projecto.valor < 0:
    #             raise ValidationError(_('Projecto value cannot be negative.'))
    #         projecto.save()
    #         super().save(*args, **kwargs)

    # Adiciona o valor do financiamento quando o projecto é deletado
    def delete(self, *args, **kwargs):
        with transaction.atomic():
            projecto = self.projecto
            projecto.valor += self.valor
            projecto.save()
            super().delete(*args, **kwargs)
