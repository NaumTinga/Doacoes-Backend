from rest_framework import serializers

from api.models.coordenador import Coordenador
from api.serializers.unidade_organica_serializers import UnidadeOrganicaSerializer


class CoordenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordenador
        fields = '__all__'


# This is to list the related classes objects not just the id's
class ListCoordenadorSerializer(serializers.ModelSerializer):
    unidade_organica = UnidadeOrganicaSerializer(read_only=True)

    class Meta:
        model = Coordenador
        fields = '__all__'
