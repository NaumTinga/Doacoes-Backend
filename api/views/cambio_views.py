from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models.cambio import Cambio
from api.serializers.cambio_serializers import CambioSerializer, CambioItemSerializer, ListCambioSerializer


class CambioViewSet(viewsets.ModelViewSet):
    queryset = Cambio.objects.all()
    serializer_class = CambioSerializer

    @action(detail=False, methods=['get'])
    def get_most_recent_cambio(self, request):
        # get_most_recent_cambio /?moeda_base = 1 & moeda_alvo = 2 // este é o link para testar o endpoint
        # Get user-provided values
        moeda_base = request.query_params.get('moeda_base')
        moeda_alvo = request.query_params.get('moeda_alvo')

        # Validate user input
        if not moeda_base or not moeda_alvo:
            return Response({'error': 'moeda_base and moeda_alvo are required parameters'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Query to retrieve the most recent Cambio object
        try:
            most_recent_cambio = Cambio.objects.filter(moeda_base=moeda_base, moeda_alvo=moeda_alvo).latest(
                'created_at')
            serializer = CambioSerializer(most_recent_cambio)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Cambio.DoesNotExist:
            return Response({'message': 'Cambio não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Log the error for debugging
            print(f"Erro inesperado: {str(e)}")
            return Response({'message': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_serializer_class(self):
        if self.action == 'create_bulk':
            return CambioItemSerializer
        return CambioSerializer

    @action(detail=False, methods=['post'])
    def create_bulk(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ListCambioSerializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ListCambioSerializer(queryset, many=True)
        return Response(serializer.data)
