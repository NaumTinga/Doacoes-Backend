from rest_framework import serializers
from api.models.unidade_organica import UnidadeOrganica


class UnidadeOrganicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeOrganica
        fields = '__all__'
