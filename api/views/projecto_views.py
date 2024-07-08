from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models.projecto import Projecto
from api.models.rubrica_projecto import RubricaProjecto
from api.serializers.projecto_serializers import ProjectoSerializer, ListProjectoSerializer
from api.serializers.rubrica_projecto_serializers import ListaRubricaProjectoSerializer


class ProjectoViewSet(viewsets.ModelViewSet):
    queryset = Projecto.objects.all()
    serializer_class = ProjectoSerializer

    # Customizing the queryset for the get by id operation
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ListProjectoSerializer(instance)
        return Response(serializer.data)

    # Customizing the queryset for the list all operation
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ListProjectoSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def rubricas_projecto(self, request, pk=None):
        projecto = self.get_object()
        rubricas_projecto = RubricaProjecto.objects.filter(projecto=projecto)
        serializer = ListaRubricaProjectoSerializer(rubricas_projecto, many=True)
        return Response(serializer.data)