from rest_framework import serializers

from api.models.assinante import Assinante


class AssinanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assinante
        fields = '__all__'