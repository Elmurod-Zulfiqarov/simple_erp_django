from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from helpers.pagination import CustomPagination
from .serializers import FarmSerializer, FAQSerializer, FodderSerializer, PetSerializer
from .models import Farm, FAQ, Fodder, Pet


class FarmViewSet(ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)


class FAQViewSet(ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)


class FodderViewSet(ModelViewSet):
    queryset = Fodder.objects.all()
    serializer_class = FodderSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("title",)
    ordering_fields = ("price", "size")

    pagination_class = CustomPagination


class PetViewSet(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("name", "purchased_date", "purchased_price")
    ordering_fields = ("pet_type", "age", "purchased_date",
                       "purchased_price", "is_sale")

    pagination_class = CustomPagination
