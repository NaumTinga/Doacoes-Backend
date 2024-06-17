from django.db import models
from api.models import coordenador, financiamento
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
    coordenador = models.ForeignKey(coordenador.Coordenador, on_delete=models.PROTECT, related_name='coordenador')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    # Este metodo verifica se o valor e as datas sao iguais ou inferiores as do financiamento
    # Data inicio e fim devem ser iguais ou inferiores ao financiamento, o valor tambem deve ser igual ou superior
    def clean(self):
        super().clean()
        if self.valor > self.financiamento.valor:
            raise ValidationError(_('Valor do Projecto não pode ser maior que o valor do Financiamento.'))

        if self.data_inicio < self.financiamento.data_inicio and self.data_fim > self.financiamento.data_fim:
            raise ValidationError(_('As datas do Projecto devem estar dentro do período das datas do Financiamento.'))

    # def save(self, *args, **kwargs):
    #     self.clean()
    #     return super().save(*args, **kwargs)

    # Cria o projecto e faz update, tendo em conta o valor do financiamento
    # subtrai e adiciona os valores do financiamento associado ao projecto
    def save(self, *args, **kwargs):
        self.clean()
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
            self._original_valor = self.valor  # Update the original valor after saving

    # # Subtrair o valor do financiamento
    # def save(self, *args, **kwargs):
    #     self.clean()
    #     with transaction.atomic():
    #         # Lock the financiamento row to prevent race conditions
    #         financiamento = self.financiamento
    #         financiamento.valor -= self.valor
    #         if financiamento.valor < 0:
    #             raise ValidationError(_('Financiamento value cannot be negative.'))
    #         financiamento.save()
    #         super().save(*args, **kwargs)

    # Adiciona o valor do financiamento quando o projecto é deletado
    def delete(self, *args, **kwargs):
        with transaction.atomic():
            financiamento = self.financiamento
            financiamento.valor += self.valor
            financiamento.save()
            super().delete(*args, **kwargs)
