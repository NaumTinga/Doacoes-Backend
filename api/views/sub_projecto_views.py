from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models.sub_projecto import SubProjecto
from api.serializers.sub_projecto_serializers import SubProjectoSerializer


class SubProjectoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = SubProjecto.objects.all()
    serializer_class = SubProjectoSerializer

    # Customizing the queryset for the get by id operation
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # Customizing the queryset for the list all operation
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
