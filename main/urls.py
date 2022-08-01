from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FarmViewSet, FAQViewSet, FodderViewSet, PetViewSet


router = DefaultRouter()

router.register("farm", FarmViewSet, basename="farm")
router.register("faq", FAQViewSet, basename="faq")
router.register("fodder", FodderViewSet, basename="fodder")
router.register("pet", PetViewSet, basename="pet")

urlpatterns = [
    path('', include(router.urls))
]
