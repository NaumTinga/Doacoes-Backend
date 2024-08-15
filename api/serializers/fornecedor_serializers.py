from rest_framework import serializers

from api.models.fornecedor import Fornecedor
from api.serializers.pais_serializers import PaisSerializer


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'


class ListFornecedorSerializer(serializers.ModelSerializer):
    pais = PaisSerializer(read_only=True)

    class Meta:
        model = Fornecedor
        fields = '__all__'
