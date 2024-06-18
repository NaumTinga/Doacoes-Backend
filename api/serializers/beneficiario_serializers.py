from rest_framework import serializers

from api.models.beneficiario import Beneficiario


class BeneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiario
        fields = '__all__'