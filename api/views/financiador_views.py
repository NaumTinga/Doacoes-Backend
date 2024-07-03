from rest_framework import viewsets
from rest_framework.response import Response

from api.models.financiador import Financiador
from api.serializers.financiador_serializers import FinanciadorSerializer, ListaFinanciadorSerializer


class FinanciadorViewSet(viewsets.ModelViewSet):
    queryset = Financiador.objects.all()
    serializer_class = FinanciadorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

        # Customizing the queryset for the list all operation

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
    # This is to list the related classes objects not just the id's
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ListaFinanciadorSerializer(queryset, many=True)
        return Response(serializer.data)
