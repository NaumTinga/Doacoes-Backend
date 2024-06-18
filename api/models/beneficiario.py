from django.db import models
import uuid
from api.models import unidade_organica, conta


class NivelAcademico(models.TextChoices):
    LICENCIATURA = 'LICENCIATURA'
    MESTRADO = 'MESTRADO'
    DOUTORAMENTO = 'DOUTORAMENTO'


class Sexo(models.TextChoices):
    MASCULINO = 'MASCULINO'
    FEMININO = 'FEMININO'


class Beneficiario(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(null=True, unique=True)
    telefone = models.CharField(max_length=255)
    data_nascimento = models.DateField(null=True)
    endereco = models.CharField(max_length=255, null=True)
    nacionalidade = models.CharField(max_length=255, null=True)
    nuit = models.BigIntegerField(null=True, unique=True)
    nivel_academico = models.CharField(
        max_length=50,
        choices=NivelAcademico.choices,
        null=True
    )
    sexo = models.CharField(max_length=50, null=True, choices=Sexo.choices)
    unidade_organica = models.ForeignKey(unidade_organica.UnidadeOrganica, on_delete=models.PROTECT, null=True,
                                         related_name='beneficiarios')
    # conta = models.ForeignKey(conta.Conta, on_delete=models.PROTECT, null=True, related_name='beneficiario_contas')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
