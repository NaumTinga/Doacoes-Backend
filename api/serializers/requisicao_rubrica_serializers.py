from rest_framework import serializers

from api.models.requisicao_rubrica import RequisicaoRubrica


class RequisicaoRubricaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequisicaoRubrica
        fields = '__all__'
