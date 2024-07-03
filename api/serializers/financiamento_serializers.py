from rest_framework import serializers

from api.models.financiamento import Financiamento
from api.serializers.financiador_serializers import FinanciadorSerializer
from api.serializers.moeda_serializers import MoedaSerializer


class FinanciamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financiamento
        fields = '__all__'

   # This is to list the related classes objects not just the id's
class ListFinanciamentoSerializer(serializers.ModelSerializer):
    moeda_financiador = MoedaSerializer(read_only=True)
    financiador = FinanciadorSerializer(read_only=True)

    class Meta:
        model = Financiamento
        fields = '__all__'
