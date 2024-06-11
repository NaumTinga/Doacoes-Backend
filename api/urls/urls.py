# banco/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.banco_views import BancoViewSet
from api.views.moeda_views import MoedaViewSet
from api.views.pais_views import PaisViewSet
from api.views.conta_views import ContaViewSet
from api.views.unidade_organica_views import UnidadeOrganicaViewSet
from api.views.coordenador_views import CoordenadorViewSet
from api.views.rubrica_estado_views import RubricaEstadoViewSet
from api.views.cambio_views import CambioViewSet
from api.views.financiador_views import FinanciadorViewSet
from api.views.rubrica_financiador_views import RubricaFinanciadorViewSet
from api.views.financiamento_views import FinanciamentoViewSet


router = DefaultRouter()
router.register(r'banco', BancoViewSet)
router.register(r'moeda', MoedaViewSet)
router.register(r'pais', PaisViewSet)
router.register(r'conta', ContaViewSet)
router.register(r'unidadeOrganica', UnidadeOrganicaViewSet)
router.register(r'coordenador', CoordenadorViewSet)
router.register(r'rubricaEstado', RubricaEstadoViewSet)
router.register(r'cambio', CambioViewSet)
router.register(r'financiador', FinanciadorViewSet)
router.register(r'rubricaFinanciador', RubricaFinanciadorViewSet)
router.register(r'financiamento', FinanciamentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cambio/create_bulk/', CambioViewSet.as_view({'post': 'create_bulk'}), name='create_bulk_cambio'),
    path('cambio/get_most_recent_cambio/', CambioViewSet.as_view({'get': 'get_most_recent_cambio'}),
         name='get_most_recent_cambio'),
]