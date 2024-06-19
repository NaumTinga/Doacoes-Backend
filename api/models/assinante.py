from django.db import models
from api.models import conta
import uuid


class TipoAssinante(models.TextChoices):
    PRINCIPAL = 'PRINCIPAL'
    SECUNDÁRIO = 'SECUNDÁRIO'
    TERCIÁRIO = 'TERCIÁRIO'
    OUTRO = 'OUTRO'


class Assinante(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length=255)
    tipo_assinante = models.CharField(max_length=20, choices=TipoAssinante, null=True)
    conta = models.ForeignKey(conta.Conta, on_delete=models.PROTECT, related_name='assinante_conta')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
