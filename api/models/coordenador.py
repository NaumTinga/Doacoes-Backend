from django.db import models
import uuid
from api.models import unidade_organica


class NivelAcademico(models.TextChoices):
    LICENCIATURA = 'LICENCIATURA'
    MESTRADO = 'MESTRADO'
    DOUTORAMENTO = 'DOUTORAMENTO'


class Sexo(models.TextChoices):
    MASCULINO = 'MASCULINO'
    FEMININO = 'FEMININO'


# Create your models here.
class Coordenador(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(null=True, unique=True)
    telefone = models.CharField(max_length=255, null=True)
    endereco = models.CharField(max_length=255, null=True)
    data_nascimento = models.DateField(null=True)
    nuit = models.BigIntegerField(null=True)
    nivel_academico = models.CharField(
        max_length=50,
        choices=NivelAcademico.choices,
        null=True
    )
    sexo = models.CharField(max_length=50, null=True, choices=Sexo.choices)
    nacionalidade = models.CharField(max_length=255, null=True)
    unidade_organica = models.ForeignKey(unidade_organica.UnidadeOrganica, on_delete=models.PROTECT, null=True,
                                         related_name='unidade_organica')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
