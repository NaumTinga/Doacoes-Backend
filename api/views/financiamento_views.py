from rest_framework import viewsets
from rest_framework.response import Response

from api.models.financiamento import Financiamento
from api.serializers.financiamento_serializers import FinanciamentoSerializer


class FinanciamentoViewSet(viewsets.ModelViewSet):
    queryset = Financiamento.objects.all()
    serializer_class = FinanciamentoSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

        # Customizing the queryset for the list all operation

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)