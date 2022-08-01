from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from helpers.pagination import CustomPagination
from .serializers import ProductSerializer, ProductRecycledSerializer
from .models import Product, ProductRecycled


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("title",)
    ordering_fields = ("product_type", "quantity", "pet", "staff")

    pagination_class = CustomPagination


class ProductRecycledViewSet(ModelViewSet):
    queryset = ProductRecycled.objects.all()
    serializer_class = ProductRecycledSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("title",)
    ordering_fields = ("price", "published_date",)

    pagination_class = CustomPagination
