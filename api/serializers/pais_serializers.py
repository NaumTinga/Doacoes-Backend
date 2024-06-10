from rest_framework import serializers
from api.models.pais import Pais


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['id', 'nome', 'sigla']
