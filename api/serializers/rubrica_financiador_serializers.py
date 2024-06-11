from rest_framework import serializers

from api.models.rubrica_financiador import RubricaFinanciador


class RubricaFinanciadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RubricaFinanciador
        fields = '__all__'