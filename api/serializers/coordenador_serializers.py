from rest_framework import serializers

from api.models.coordenador import Coordenador


class CoordenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordenador
        fields = '__all__'