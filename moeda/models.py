from django.db import models


# Create your models here.
class Moeda(models.Model):
    designacao = models.CharField(max_length=100)
    sigla = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.designacao