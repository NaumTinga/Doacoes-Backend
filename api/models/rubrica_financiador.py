from django.db import models
import uuid
from api.models import financiador


class RubricaFinanciador(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    codigo_rubrica = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    financiador = models.ForeignKey(financiador.Financiador, on_delete=models.PROTECT, related_name='financiador')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nome