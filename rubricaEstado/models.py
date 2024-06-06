from django.db import models

# Create your models here.
class RubricaEstado(models.Model):
    class TipoRubrica(models.TextChoices):
        FUNCIONAMENTO = 'FUNCIONAMENTO',
        INVESTIMENTO = 'INVESTIMENTO'

    codigo = models.BigIntegerField()
    nome = models.CharField(max_length=255)
    tipoRubrica = models.CharField(max_length=20, choices=TipoRubrica.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    