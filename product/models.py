from django.db import models
from account.models import Staff
from helpers.models import BaseModel
from main.models import Pet

MILK = "milk"
MEAT = "meat"
OTHER = "other"

PRODUCT_CHOICES = (
    (MILK, "milk"),
    (MEAT, "meat"),
    (OTHER, "other")
)


class Product(BaseModel):
    title = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    product_type = models.CharField(choices=PRODUCT_CHOICES, max_length=32)
    quantity = models.CharField(max_length=32, null=True, blank=True)

    pet = models.ForeignKey(
        Pet, on_delete=models.DO_NOTHING, related_name='product')
    staff = models.ForeignKey(
        Staff, on_delete=models.DO_NOTHING, related_name="product")

    published_date = models.DateField(auto_now_add=True)
    sold_out_price = models.CharField(
        max_length=32, null=True, blank=True)

    def __str__(self):
        return f"{self.published_date} kun /{self.liters} liter sut"


class ProductRecycled(BaseModel):
    title = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(null=True, blank=False)
    image = models.ImageField(
        upload_to="media/product_recycled", null=True, blank=True)

    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, related_name="product_recycled")
    price = models.CharField(max_length=32, null=True, blank=True)

    published_date = models.DateField(auto_now_add=True)
    purchased_date = models.DateField(null=True, blank=True)
