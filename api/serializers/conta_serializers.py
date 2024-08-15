from rest_framework import serializers

from api.models.conta import Conta
from api.serializers.banco_serializers import BancoSerializer
from api.serializers.beneficiario_serializers import BeneficiarioSerializer
from api.serializers.financiador_serializers import FinanciadorSerializer
from api.serializers.moeda_serializers import MoedaSerializer


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = '__all__'


class ListContaSerializer(serializers.ModelSerializer):
    banco = BancoSerializer(read_only=True)
    moeda = MoedaSerializer(read_only=True)
    financiador = FinanciadorSerializer(read_only=True)
    beneficiario = BeneficiarioSerializer(read_only=True)

    class Meta:
        model = Conta
        fields = '__all__'
