from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models.beneficiario import Beneficiario
from api.models.conta import Conta
from api.serializers.beneficiario_serializers import BeneficiarioSerializer, ListBeneficiarioSerializer
from api.serializers.conta_serializers import ContaSerializer, ListContaSerializer


class BeneficiarioViewSet(viewsets.ModelViewSet):
    queryset = Beneficiario.objects.all()
    serializer_class = BeneficiarioSerializer

    @action(detail=True, methods=['get'])
    def contas(self, request, pk=None):
        beneficiario = self.get_object()
        contas = Conta.objects.filter(beneficiario=beneficiario)
        serializer = ListContaSerializer(contas, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ListBeneficiarioSerializer(instance)
        return Response(serializer.data)

    # New List
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ListBeneficiarioSerializer(queryset, many=True)
        return Response(serializer.data)

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    # Customizing the queryset for the list all operation

    # Old list
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
