from rest_framework import serializers

from api.models.ordem_pagamento_rubrica import OrderPagamentoRubrica
from api.serializers.assinante_serializers import AssinanteSerializer
from api.serializers.conta_serializers import ContaSerializer
from api.serializers.fornecedor_serializers import FornecedorSerializer
from api.serializers.sub_rubrica_serializers import SubRubricaSerializer


class OrderPagamentoRubricaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPagamentoRubrica
        fields = '__all__'


class ListOrderPagamentoRubricaSerializer(serializers.ModelSerializer):
    sub_rubrica = SubRubricaSerializer(read_only=True)
    fornecedor = FornecedorSerializer(read_only=True)
    conta_ordenador = ContaSerializer(read_only=True)
    assinante_principal = AssinanteSerializer(read_only=True)

    class Meta:
        model = OrderPagamentoRubrica
        fields = '__all__'
