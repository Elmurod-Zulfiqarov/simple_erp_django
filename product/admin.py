from django.contrib import admin

from product.models import Product, ProductRecycled

admin.site.register([Product, ProductRecycled])
