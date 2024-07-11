from rest_framework import serializers

from api.models.sub_projecto import SubProjecto
from api.serializers.moeda_serializers import MoedaSerializer
from api.serializers.rubrica_projecto_serializers import RubricaProjectoSerializer


class SubProjectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubProjecto
        fields = '__all__'


# class ListSubProjectosSerializer(serializers.ModelSerializer):
#     moeda_sub_projecto = MoedaSerializer(read_only=True)
#
#     class Meta:
#         model = SubProjecto
#         fields = '__all__'
