from django.contrib import admin

from api.models.actividade import Actividade
from api.models.assinante import Assinante
from api.models.banco import Banco
from api.models.beneficiario import Beneficiario
from api.models.cambio import Cambio
from api.models.conta import Conta
from api.models.coordenador import Coordenador
from api.models.distribuicao import Distribuicao
from api.models.financiador import Financiador
from api.models.financiamento import Financiamento
from api.models.fornecedor import Fornecedor
from api.models.moeda import Moeda
from api.models.ordem_pagamento_rubrica import OrderPagamentoRubrica
from api.models.pais import Pais
from api.models.projecto import Projecto
from api.models.requisicao import Requisicao
from api.models.requisicao_rubrica import RequisicaoRubrica
from api.models.rubrica_estado import RubricaEstado
from api.models.rubrica_financiador import RubricaFinanciador
from api.models.rubrica_projecto import RubricaProjecto
from api.models.sub_projecto import SubProjecto
from api.models.unidade_organica import UnidadeOrganica

# Register your models here.
admin.site.register(Actividade)
admin.site.register(Assinante)
admin.site.register(Banco)
admin.site.register(Beneficiario)
admin.site.register(Cambio)
admin.site.register(Conta)
admin.site.register(Coordenador)
admin.site.register(Distribuicao)
admin.site.register(Financiador)
admin.site.register(Financiamento)
admin.site.register(Fornecedor)
admin.site.register(Moeda)
admin.site.register(OrderPagamentoRubrica)
admin.site.register(Pais)
admin.site.register(Projecto)
admin.site.register(Requisicao)
admin.site.register(RequisicaoRubrica)
admin.site.register(RubricaEstado)
admin.site.register(RubricaFinanciador)
admin.site.register(RubricaProjecto)
admin.site.register(SubProjecto)
admin.site.register(UnidadeOrganica)
