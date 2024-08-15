from rest_framework import serializers

from api.models.ordem_pagamento_rubrica import OrderPagamentoRubrica


class OrderPagamentoRubricaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPagamentoRubrica
        fields = '__all__'
