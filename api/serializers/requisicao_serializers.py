from rest_framework import serializers

from api.models.requisicao import Requisicao


class RequisicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisicao
        fields = '__all__'
