from django.db import models, transaction
import uuid

from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from api.models import rubrica_estado, rubrica_financiador, sub_projecto


class Eixo(models.TextChoices):
    EEA = 'EEA', 'Eixo de Ensino e Aprendizagem',
    EI = 'EI', 'Eixo de Investigaçao',
    EEIU = 'EEIU', 'Eixo de Extensão e Inovação Universitárias',
    EGCU = 'EGCU', 'Eixo de Governação e Cooperação Universitárias',
    EGFRH = 'EGFRH', 'Eixo de Gestão, Finanças e Recursos Humanos',
    EPI = 'EPI', 'Eixo de Patrimônio e Infra-estruturas',
    EAT = 'EAT', 'Eixo de Assuntos Transversais'


class Distribuicao(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    valor = models.DecimalField(max_digits=20, decimal_places=3)
    descricao = models.CharField(max_length=255)
    eixo = models.CharField(
        max_length=244,
        choices=Eixo.choices,
        null=False, blank=False
    )
    rubrica_estado = models.ForeignKey(rubrica_estado.RubricaEstado, on_delete=models.PROTECT,
                                       related_name='distribuica_rubrica_estado', null=False, blank=False)
    rubrica_financiador = models.ForeignKey(rubrica_financiador.RubricaFinanciador, on_delete=models.PROTECT,
                                            related_name='distribuica_rubrica_financiador', null=True)
    sub_projecto = models.ForeignKey(sub_projecto.SubProjecto, on_delete=models.PROTECT, null=False, blank=False,
                                     related_name='distribuicao_sub_projecto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descricao

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._original_valor = self.valor if self.pk else None

    def clean(self):
        super().clean()
        if self.valor > self.sub_projecto.valor:
            raise ValidationError(_('O valor da Distribuição não pode ser maior que o valor do SubProjecto.'))

    def save(self, *args, **kwargs):
        self.clean()
        with transaction.atomic():
            sub_projecto = self.sub_projecto

            if self.pk is not None:
                # Update case
                old_valor = Distribuicao.objects.get(pk=self.pk).valor
                valor_difference = self.valor - old_valor
                sub_projecto.valor -= valor_difference
            else:
                # Create case
                sub_projecto.valor -= self.valor

            if sub_projecto.valor < 0:
                raise ValidationError(_('O valor do SubProjecto não pode ser negativo.'))

            sub_projecto.save()
            super().save(*args, **kwargs)
            self._original_valor = self.valor

    def delete(self, *args, **kwargs):
        with transaction.atomic():
            sub_projecto = self.sub_projecto
            sub_projecto.valor += self.valor
            sub_projecto.save()
            super().delete(*args, **kwargs)
