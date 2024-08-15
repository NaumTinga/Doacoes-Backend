from rest_framework import serializers
from api.models.cambio import Cambio
from api.serializers.moeda_serializers import MoedaSerializer


class CambioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cambio
        fields = '__all__'


class ListCambioSerializer(serializers.ModelSerializer):
    moeda_base = MoedaSerializer(read_only=True)
    moeda_alvo = MoedaSerializer(read_only=True)
    class Meta:
        model = Cambio
        fields = '__all__'


class BulkCambioSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        cambios = [Cambio(**item) for item in validated_data]
        return Cambio.objects.bulk_create(cambios)


class CambioItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cambio
        fields = '__all__'
        list_serializer_class = BulkCambioSerializer
