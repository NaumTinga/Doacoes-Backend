from django.db import models


# Create your models here.
class UnidadeOrganica(models.Model):
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
