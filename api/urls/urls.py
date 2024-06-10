# banco/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.banco_views import BancoViewSet
from api.views.moeda_views import MoedaViewSet
from api.views.pais_views import PaisViewSet
from api.views.conta_central_views import ContaCentralViewSet
from api.views.unidade_organica_views import UnidadeOrganicaViewSet
from api.views.coordenador_views import CoordenadorViewSet
from api.views.rubrica_estado_views import RubricaEstadoViewSet


router = DefaultRouter()
router.register(r'banco', BancoViewSet)
router.register(r'moeda', MoedaViewSet)
router.register(r'pais', PaisViewSet)
router.register(r'contaCentral', ContaCentralViewSet)
router.register(r'unidadeOrganica', UnidadeOrganicaViewSet)
router.register(r'coordenador', CoordenadorViewSet)
router.register(r'rubricaEstado', RubricaEstadoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]