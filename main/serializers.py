from rest_framework.serializers import ModelSerializer
from .models import Farm, FAQ, Fodder, Pet


class FarmSerializer(ModelSerializer):

    class Meta:
        model = Farm
        fields = '__all__'


class FAQSerializer(ModelSerializer):

    class Meta:
        model = FAQ
        fields = '__all__'


class FodderSerializer(ModelSerializer):

    class Meta:
        model = Fodder
        fields = '__all__'


class PetSerializer(ModelSerializer):

    class Meta:
        model = Pet
        fields = '__all__'
