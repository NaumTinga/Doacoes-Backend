from django.db import models
import uuid


class TipoRubrica(models.TextChoices):
    INVESTIMENTO = 'INVESTIMENTO'
    FUNCIONAMENTO = 'FUNCIONAMENTO'


class RubricaEstado(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    tipo_rubrica = models.CharField(max_length=55, null=False, blank=False, choices=TipoRubrica.choices)
    codigo_rubrica = models.CharField(max_length=55)
    nome = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
