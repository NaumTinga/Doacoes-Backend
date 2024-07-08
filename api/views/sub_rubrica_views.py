from rest_framework import viewsets
from rest_framework.response import Response

from api.models.sub_rubrica import SubRubrica
from api.serializers.sub_rubrica_serializers import SubRubricaSerializer


class SubRubricaViewSet(viewsets.ModelViewSet):
    queryset = SubRubrica.objects.all()
    serializer_class = SubRubricaSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SubRubricaSerializer(instance)
        return Response(serializer.data)

        # Customizing the queryset for the list all operation

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = SubRubricaSerializer(queryset, many=True)
        return Response(serializer.data)