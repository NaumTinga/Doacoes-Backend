from rest_framework import serializers
from .models import RubricaEstado


class RubricaEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RubricaEstado
        fields = '__all__'