from rest_framework import serializers
from .models import Moeda


class MoedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moeda
        # fields = '__all__'
        fields = ["id", "designacao", "sigla", "created_at", "updated_at"]
