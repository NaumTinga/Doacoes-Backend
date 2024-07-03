from rest_framework import viewsets
from rest_framework.response import Response

from api.models.projecto import Projecto
from api.serializers.projecto_serializers import ProjectoSerializer, ListProjectoSerializer


class ProjectoViewSet(viewsets.ModelViewSet):
    queryset = Projecto.objects.all()
    serializer_class = ProjectoSerializer

    # Customizing the queryset for the get by id operation
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
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
