from rest_framework import serializers

from api.models.requisicao_rubrica import RequisicaoRubrica
from api.serializers.fornecedor_serializers import FornecedorSerializer
from api.serializers.moeda_serializers import MoedaSerializer
from api.serializers.rubrica_estado_serializers import RubricaEstadoSerializer
from api.serializers.rubrica_projecto_serializers import RubricaProjectoSerializer
from api.serializers.sub_rubrica_serializers import SubRubricaSerializer


class RequisicaoRubricaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequisicaoRubrica
        fields = '__all__'


class ListaRequisicaoRubricaSerializer(serializers.ModelSerializer):
    rubrica_projecto = RubricaProjectoSerializer(read_only=True)
    sub_rubrica = SubRubricaSerializer(read_only=True)
    moeda_requisicao = MoedaSerializer(read_only=True)
    fornecedor = FornecedorSerializer(read_only=True)
    rubrica_estado = RubricaEstadoSerializer(read_only=True)

    class Meta:
        model = RequisicaoRubrica
        fields = '__all__'
