# banco/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BancoViewSet


router = DefaultRouter()
router.register(r'banco', BancoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]