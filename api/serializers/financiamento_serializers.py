from rest_framework import serializers

from api.models.financiamento import Financiamento


class FinanciamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financiamento
        fields = '__all__'