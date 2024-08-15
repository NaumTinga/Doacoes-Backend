from rest_framework import serializers

from api.models.beneficiario import Beneficiario
from api.serializers.unidade_organica_serializers import UnidadeOrganicaSerializer


class BeneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiario
        fields = '__all__'


class ListBeneficiarioSerializer(serializers.ModelSerializer):
    unidade_organica = UnidadeOrganicaSerializer(read_only=True)

    class Meta:
        model = Beneficiario
        fields = '__all__'
