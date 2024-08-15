from rest_framework import serializers

from api.models.financiador import Financiador
from api.serializers.pais_serializers import PaisSerializer


class FinanciadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financiador
        fields = '__all__'


# This is to list the related classes objects not just the id's
class ListaFinanciadorSerializer(serializers.ModelSerializer):
    pais = PaisSerializer(read_only=True)

    class Meta:
        model = Financiador
        fields = '__all__'
