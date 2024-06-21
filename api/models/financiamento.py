from django.db import models
import uuid
from api.models import conta, financiador, moeda


class Financiamento(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor = models.DecimalField(max_digits=50, decimal_places=3)
    conta_destino = models.ForeignKey(conta.Conta, on_delete=models.PROTECT, related_name='conta_destino')
    descricao = models.CharField(max_length=255)
    conta_origem = models.ForeignKey(conta.Conta, on_delete=models.PROTECT, related_name='conta_origem')
    # Para saber qual moeda distribuir, definir este field no front
    moeda_financiador = models.ForeignKey(moeda.Moeda, on_delete=models.PROTECT, related_name='moeda_financiador',
                                          null=True)
    financiador = models.ForeignKey(financiador.Financiador, on_delete=models.PROTECT, related_name='financiador_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descricao
