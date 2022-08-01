from django.db import models
from account.models import Staff
from helpers.models import BaseModel


class Farm(BaseModel):
    title = models.CharField(max_length=128, null=True, blank=True)
    sub_content = models.CharField(max_length=512, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)
    images = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title


class FAQ(BaseModel):
    title = models.CharField(max_length=128)
    question = models.CharField(max_length=512)
    answer = models.TextField(null=True, blank=True)


BULL = "bull"
COW = "cow"
CALF = "calf"

PET_CHOICES = (
    (BULL, 'bull'),
    (COW, 'cow'),
    (CALF, 'calf'),
)


class Pet(BaseModel):
    name = models.CharField(max_length=128)
    pet_type = models.CharField(max_length=30, choices=PET_CHOICES)
    image = models.ImageField(upload_to="media/pet", null=True, blank=False)
    age = models.FloatField()
    weight = models.FloatField()

    purchased_date = models.DateField(blank=False)
    purchased_price = models.CharField(max_length=32, null=True, blank=False)

    sold_out_date = models.DateField(null=True, blank=False)
    sold_out_price = models.CharField(
        max_length=32, null=True, blank=True)

    is_sale = models.BooleanField(default=False)
    sale_price = models.CharField(max_length=32, null=True, blank=False)

    staff = models.ForeignKey(
        Staff, on_delete=models.DO_NOTHING, related_name="pet")

    def __str__(self):
        return self.name


class Fodder(BaseModel):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=False)
    price = models.CharField(max_length=32, null=True, blank=False)
    size = models.CharField(max_length=16, null=True, blank=False)

    purchased_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
