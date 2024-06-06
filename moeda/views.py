from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response

from moeda.models import Moeda
from moeda.serializers import MoedaSerializer


# Create your views here.
class MoedaViewSet(viewsets.ModelViewSet):
    queryset = Moeda.objects.all()
    serializer_class = MoedaSerializer

    # Customizing the queryset for the get by id operation
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # Customizing the queryset for the list all operation
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# Old views, generics
# class MoedaListCreate(generics.ListCreateAPIView):
#     queryset = Moeda.objects.all()
#     serializer_class = MoedaSerializer
#
# class MoedaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Moeda.objects.all()
#     serializer_class = MoedaSerializer
#     lookup_field = 'pk'
