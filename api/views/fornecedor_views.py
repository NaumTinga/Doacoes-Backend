from rest_framework import viewsets
from rest_framework.response import Response

from api.models.fornecedor import Fornecedor
from api.serializers.fornecedor_serializers import FornecedorSerializer, ListFornecedorSerializer


class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

        # Customizing the queryset for the list all operation

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ListFornecedorSerializer(queryset, many=True)
        return Response(serializer.data)
