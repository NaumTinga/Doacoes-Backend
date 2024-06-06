from django.db import models

# Create your models here.
class RubricaEstado(models.Model):
    codigo = models.BigIntegerField()
    nome = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    