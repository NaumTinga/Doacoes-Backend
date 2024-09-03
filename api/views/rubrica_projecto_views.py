from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models.rubrica_projecto import RubricaProjecto
from api.models.sub_rubrica import SubRubrica
from api.serializers.rubrica_projecto_serializers import RubricaProjectoSerializer, ListaRubricaProjectoSerializer
from api.serializers.sub_rubrica_serializers import ListSubRubricaSerializer


class RubricaProjectoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = RubricaProjecto.objects.all()
    serializer_class = RubricaProjectoSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ListaRubricaProjectoSerializer(instance)
        return Response(serializer.data)

    # Customizing the queryset for the list all operation
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ListaRubricaProjectoSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def sub_rubricas_projecto(self, request, pk=None):
        rubrica_projecto = self.get_object()
        sub_rubricas = SubRubrica.objects.filter(rubrica_projecto=rubrica_projecto)
        serializer = ListSubRubricaSerializer(sub_rubricas, many=True)
        return Response(serializer.data)
