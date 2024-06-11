from rest_framework import serializers

from api.models.actividade import Actividade


class ActividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividade
        fields = '__all__'
