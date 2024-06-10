from rest_framework import serializers

from api.models.rubrica_estado import RubricaEstado


class RubricaEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RubricaEstado
        fields = '__all__'