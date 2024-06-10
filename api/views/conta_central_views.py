from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from api.models.conta_central import ContaCentral
from api.serializers.conta_central_serializers import ContaCentralSerializer


# Create your views here.
class ContaCentralViewSet(viewsets.ModelViewSet):
    queryset = ContaCentral.objects.all()
    serializer_class = ContaCentralSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

        # Customizing the queryset for the list all operation

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

