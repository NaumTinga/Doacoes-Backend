from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models.ordem_pagamento_rubrica import OrderPagamentoRubrica
from api.serializers.ordem_pagamento_rubrica_serializers import OrderPagamentoRubricaSerializer, \
    ListOrderPagamentoRubricaSerializer


class OrderPagamentoRubricaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = OrderPagamentoRubrica.objects.all()
    serializer_class = OrderPagamentoRubricaSerializer

    # Customizing the queryset for the get by id operation
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = OrderPagamentoRubricaSerializer(instance)
        return Response(serializer.data)

    # Customizing the queryset for the list all operation
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ListOrderPagamentoRubricaSerializer(queryset, many=True)
        return Response(serializer.data)
