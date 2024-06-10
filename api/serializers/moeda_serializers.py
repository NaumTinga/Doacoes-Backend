from rest_framework import serializers
from api.models.moeda import Moeda


class MoedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moeda
        fields = '__all__'
