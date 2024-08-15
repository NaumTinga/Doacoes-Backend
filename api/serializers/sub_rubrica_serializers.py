from rest_framework import serializers

from api.models.rubrica_projecto import RubricaProjecto
from api.models.sub_rubrica import SubRubrica
from api.serializers.moeda_serializers import MoedaSerializer


class SubRubricaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubRubrica
        fields = '__all__'


class ListSubRubricaSerializer(serializers.ModelSerializer):
    moeda_sub_rubrica = MoedaSerializer(read_only=True)

    class Meta:
        model = SubRubrica
        fields = '__all__'
