from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from api.models.conta import Conta
from api.serializers.conta_serializers import ContaSerializer, ListContaSerializer


# Create your views here.
class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

        # Customizing the queryset for the list all operation

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ListContaSerializer(queryset, many=True)
        return Response(serializer.data)
