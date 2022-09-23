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

    # @action(detail=False, methods=['get'], url_path='types/<int:idrange>/')
    # def get_models(self, request, *args, **kwargs):
    #     idrange=int(kwargs['idrange'])
    #     res=Models.objects.filter(idrange=idrange)
    #     print(res.values_list())
    #     return Response(res.values())
    #
    #
    # @action(detail=True, methods=['post'])
    # def add_models(self, request, *args, **kwargs):
    #     self.http_method_names.append("GET")
    #     idrange=int(kwargs['idrange'])
    #     idrange=Range.objects.filter(rangeid=idrange)[0]
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         # Models.objects.create(idrange=idrange,
    #         #                       modelname=serializer['modelname'].to_python(),
    #         #                       producer=serializer['producer'].to_python(),
    #         #                       # price=serializer['price'],
    #         #                       price=15000,
    #         #                       image=serializer['image'].to_python())
    #         serializer.save()
    #         return Response(status=status.HTTP_200_OK)
    #     else:
    #         print(serializer.errors)
    #         return Response(status=status.HTTP_400_BAD_REQUEST)

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all().order_by('idmodel')
    serializer_class = StockSerializer


class ModelsOfTypeViewSet(viewsets.ModelViewSet):
    serializer_class = ModelsSerializer

    def get_queryset(self):
        print(self.kwargs['types_pk'])
        queryset = Models.objects.filter(idrange=self.kwargs['types_pk'])
        return queryset

class StockOfModelViewSet(viewsets.ModelViewSet):
    serializer_class = StockSerializer
    def get_queryset(self):
        queryset = Stock.objects.filter(idmodel=self.kwargs['models_pk'])
        return queryset

#
# class RangeModelViewSet(viewsets.ModelViewSet):
#     def __init__(self, idrange):
#         queryset = Models.objects.filter(idrange=idrange)
#         serializer_class = ModelsSerializer
#
#
