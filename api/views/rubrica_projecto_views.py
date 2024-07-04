from rest_framework import viewsets
from rest_framework.response import Response

from api.models.rubrica_projecto import RubricaProjecto
from api.serializers.rubrica_projecto_serializers import RubricaProjectoSerializer, ListaRubricaProjectoSerializer


class RubricaProjectoViewSet(viewsets.ModelViewSet):
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
