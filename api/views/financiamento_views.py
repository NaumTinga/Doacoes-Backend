from rest_framework import viewsets
from rest_framework.response import Response

from api.models.financiamento import Financiamento
from api.serializers.financiamento_serializers import FinanciamentoSerializer, ListFinanciamentoSerializer


class FinanciamentoViewSet(viewsets.ModelViewSet):
    queryset = Financiamento.objects.all()
    serializer_class = FinanciamentoSerializer

    # Old get method
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    # new get method to show all related classes object attributes
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ListFinanciamentoSerializer(instance)
        return Response(serializer.data)

        # Customizing the queryset for the list all operation

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # This is to list the related classes objects not just the id's
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ListFinanciamentoSerializer(queryset, many=True)
        return Response(serializer.data)