from django.shortcuts import render
from rest_framework import viewsets
from shop100.serializers import RangeSerializer, ModelsSerializer, StockSerializer
from shop100.models import Range, Models, Stock

class RangeViewSet(viewsets.ModelViewSet):
    queryset = Range.objects.all().order_by('rangename')
    serializer_class = RangeSerializer

class ModelsViewSet(viewsets.ModelViewSet):
    queryset = Models.objects.all().order_by('idrange', 'modelname')
    serializer_class = ModelsSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all().order_by('idmodel')
    serializer_class = StockSerializer
#
# class RangeModelViewSet(viewsets.ModelViewSet):
#     def __init__(self, idrange):
#         queryset = Models.objects.filter(idrange=idrange)
#         serializer_class = ModelsSerializer
#
#
