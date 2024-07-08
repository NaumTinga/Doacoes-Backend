from rest_framework import serializers

from api.models.projecto import Projecto
from api.serializers.coordenador_serializers import CoordenadorSerializer
from api.serializers.financiamento_serializers import FinanciamentoSerializer
from api.serializers.rubrica_projecto_serializers import RubricaProjectoSerializer
from api.serializers.sub_projecto_serializers import SubProjectoSerializer


class ProjectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projecto
        fields = '__all__'


class ListProjectoSerializer(serializers.ModelSerializer):
    financiamento = FinanciamentoSerializer(read_only=True)
    coordenador = CoordenadorSerializer(read_only=True)


    class Meta:
        model = Projecto
        fields = '__all__'
