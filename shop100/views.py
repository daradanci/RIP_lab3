from django.shortcuts import render
from rest_framework import viewsets, serializers, status
from shop100.serializers import RangeSerializer, ModelsSerializer, StockSerializer
from shop100.models import Range, Models, Stock
from rest_framework.decorators import action
from rest_framework.response import Response
class RangeViewSet(viewsets.ModelViewSet):
    queryset = Range.objects.all().order_by('rangename')
    serializer_class = RangeSerializer

class ModelsViewSet(viewsets.ModelViewSet):
    queryset = Models.objects.all().order_by('idrange', 'modelname')
    serializer_class = ModelsSerializer

    @action(detail=False, methods=['get'])
    def get_models(self, request, *args, **kwargs):
        idrange=int(kwargs['idrange'])
        res=Models.objects.filter(idrange=idrange)
        print(res.values_list())
        return Response(res.values())

    @action(detail=True, methods=['post'])
    def add_models(self, request, *args, **kwargs):
        idrange=int(kwargs['idrange'])
        serializer = self.get_serializer(data=request.data)
        Models.objects.create(idrange=idrange,
                              modelname=serializer['modelname'],
                              producer=serializer['producer'],
                              price=serializer['price'],
                              image=serializer['image'])
        return Response(status=status.HTTP_204_NO_CONTENT)

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
