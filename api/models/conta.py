from django.db import models
import uuid
from api.models import banco, moeda, beneficiario, financiador


# Create your models here.
class Conta(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    designacao = models.CharField(max_length=255)
    nr_conta = models.IntegerField()
    nib = models.CharField(max_length=255, null=True)
    swift = models.CharField(max_length=255, null=True)
    iban = models.CharField(max_length=255, null=True)
    balcao = models.CharField(max_length=255, null=True)
    banco = models.ForeignKey(banco.Banco, on_delete=models.PROTECT, null=True, related_name='conta_banco')
    moeda = models.ForeignKey(moeda.Moeda, on_delete=models.PROTECT, null=True, related_name='conta_moeda')
    beneficiario = models.ForeignKey(beneficiario.Beneficiario, on_delete=models.PROTECT, null=True,
                                     related_name='beneficiario_contas')
    financiador = models.ForeignKey(financiador.Financiador, on_delete=models.PROTECT, null=True, related_name='conta_financiador')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.designacao
