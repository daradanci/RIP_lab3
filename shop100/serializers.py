from shop100.models import Range, Models, Stock
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer
from rest_framework_nested.relations import NestedHyperlinkedRelatedField


class RangeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Range
        fields = ["rangeid", "rangename"]



class ModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Models
        fields = ["modelid", "idrange", "modelname", "producer", "price", "image"]



class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stock
        fields=["itemid", "idmodel", "size", "amount"]