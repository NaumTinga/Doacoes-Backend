from rest_framework import serializers
from api.models.rubrica_projecto import RubricaProjecto


class RubricaProjectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RubricaProjecto
        fields = '__all__'


class ListaRubricaProjectoSerializer(serializers.ModelSerializer):
    projecto = serializers.StringRelatedField()

    class Meta:
        model = RubricaProjecto
        fields = '__all__'
