# unidadeOrganica/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UnidadeOrganicaViewSet

router = DefaultRouter()
router.register(r'unidadeOrganica', UnidadeOrganicaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]