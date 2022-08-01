from rest_framework.serializers import ModelSerializer
from .models import Product, ProductRecycled


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductRecycledSerializer(ModelSerializer):

    class Meta:
        model = ProductRecycled
        fields = '__all__'
