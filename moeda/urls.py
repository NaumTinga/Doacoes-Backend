# moeda/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MoedaViewSet


router = DefaultRouter()
router.register(r'moeda', MoedaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]