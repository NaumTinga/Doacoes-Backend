from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models.actividade import Actividade
from api.serializers.actividade_serializers import ActividadeSerializer


class ActividadeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Actividade.objects.all()
    serializer_class = ActividadeSerializer

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
