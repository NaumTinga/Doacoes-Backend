from rest_framework import serializers

from api.models.distribuicao import Distribuicao


class DistribuicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distribuicao
        fields = '__all__'
