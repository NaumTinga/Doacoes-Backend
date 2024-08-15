from rest_framework import viewsets
from rest_framework.response import Response

from api.models.requisicao_rubrica import RequisicaoRubrica
from api.serializers.requisicao_rubrica_serializers import RequisicaoRubricaSerializer, ListaRequisicaoRubricaSerializer


class RequisicaoRubricaViewSet(viewsets.ModelViewSet):
    queryset = RequisicaoRubrica.objects.all()
    serializer_class = RequisicaoRubricaSerializer

    # Customizing the queryset for the get by id operation
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ListaRequisicaoRubricaSerializer(instance)
        return Response(serializer.data)

    # Customizing the queryset for the list all operation
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ListaRequisicaoRubricaSerializer(queryset, many=True)
        return Response(serializer.data)
