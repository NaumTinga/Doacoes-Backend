from django.db import models
import uuid
from api.models import pais


class Financiador(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True)
    endereco = models.CharField(max_length=255, null=True)
    telefone = models.BigIntegerField(null=True)
    pais = models.ForeignKey(pais.Pais, on_delete=models.PROTECT, null=True,
                             related_name='pais')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
