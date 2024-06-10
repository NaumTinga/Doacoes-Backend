from rest_framework import viewsets
from rest_framework.response import Response

from api.models.moeda import (Moeda)
from api.serializers.moeda_serializers import MoedaSerializer


class MoedaViewSet(viewsets.ModelViewSet):
    serializer_class = MoedaSerializer
    queryset = Moeda.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

        # Customizing the queryset for the list all operation

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)