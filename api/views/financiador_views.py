from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import financiador
from api.models.conta import Conta
from api.models.financiador import Financiador
from api.models.financiamento import Financiamento
from api.serializers.conta_serializers import ListContaSerializer
from api.serializers.financiador_serializers import FinanciadorSerializer, ListaFinanciadorSerializer
from api.serializers.financiamento_serializers import ListFinanciamentoSerializer


class FinanciadorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Financiador.objects.all()
    serializer_class = FinanciadorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ListaFinanciadorSerializer(instance)
        return Response(serializer.data)

        # Customizing the queryset for the list all operation

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ListaFinanciadorSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def contas(self, request, pk=None):
        financiador = self.get_object()
        contas = Conta.objects.filter(financiador=financiador)
        serializer = ListContaSerializer(contas, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def financiamentos(self, request, pk=None):
        financiador = self.get_object()
        financiamentos = Financiamento.objects.filter(financiador=financiador)
        serializer = ListFinanciamentoSerializer(financiamentos, many=True)
        return Response(serializer.data)

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
    # This is to list the related classes objects not just the id's