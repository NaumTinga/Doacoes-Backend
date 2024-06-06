from rest_framework import serializers
from .models import UnidadeOrganica


class UnidadeOrganicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeOrganica
        fields = '__all__'