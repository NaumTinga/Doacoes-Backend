from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models.requisicao_rubrica import RequisicaoRubrica, EstadoPagamento
from api.serializers.requisicao_rubrica_serializers import RequisicaoRubricaSerializer, ListaRequisicaoRubricaSerializer


class RequisicaoRubricaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
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

    @action(detail=False, methods=['put'], url_path='update-estado')
    def update_estado_pagamento(self, request):
        """
        Custom endpoint to update the estado_pagamento of multiple RequisicaoRubrica records.
        """
        # Extracting IDs and estado_pagamento from the request data
        ids = request.data.get('ids', [])
        estado_pagamento = request.data.get('estado')

        if not ids or not estado_pagamento:
            return Response(
                {"error": "IDs and estado_pagamento are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Filter the queryset for the provided IDs
        queryset = RequisicaoRubrica.objects.filter(id__in=ids)

        # Update the estado_pagamento for all matching requisicoes
        updated_count = queryset.update(estado_pagamento=EstadoPagamento.PENDENTE)

        if updated_count == 0:
            return Response(
                {"error": "No requisicoes were updated."},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            {"message": f"{updated_count} requisicoes updated successfully."},
            status=status.HTTP_200_OK
        )