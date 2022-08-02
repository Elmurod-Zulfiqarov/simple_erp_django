from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from helpers.pagination import CustomPagination
from .serializers import StaffSerializer
from .models import Staff


class StaffViewSet(ModelViewSet):
    serializer_class = StaffSerializer

    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("full_name", "specialty", "phone")
    ordering_fields = ("gender", "salary", "specialty")

    pagination_class = CustomPagination

    def get_queryset(self):
        return Staff.objects.all().select_related('user')
