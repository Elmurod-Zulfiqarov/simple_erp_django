from django.db import models
from common.models import User
from helpers.models import BaseModel


FEMALE = "female"
MALE = "male"

GENdDER_CHOICES = (
    (FEMALE, "female"),
    (MALE, "male")
)


class Staff(BaseModel):
    full_name = models.CharField(max_length=256)
    definition = models.TextField(max_length=4096, null=True, blank=True)
    image = models.ImageField(upload_to="account/stuff", null=True, blank=True)

    specialty = models.CharField(max_length=256)
    salary = models.CharField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="staff")

    gender = models.CharField(choices=GENdDER_CHOICES, max_length=8)
    passport = models.FileField(null=True, blank=True)

    phone = models.CharField(max_length=32, null=True, blank=True)
    phone_farm = models.CharField(max_length=32, null=True, blank=True)
    telegram = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.full_name
