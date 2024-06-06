# rubricaEstado/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RubricaEstadoViewSet


router = DefaultRouter()
router.register(r'rubricaEstado', RubricaEstadoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]