from rest_framework import serializers

from api.models.financiador import Financiador


class FinanciadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financiador
        fields = '__all__'
