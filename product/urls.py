from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductRecycledViewSet


router = DefaultRouter()

router.register("product", ProductViewSet, basename="product")
router.register("re-product", ProductRecycledViewSet, basename="re-product")

urlpatterns = [
    path('', include(router.urls))
]
