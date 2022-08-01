from django.contrib import admin

from main.models import Farm, FAQ, Pet, Fodder

admin.site.register([Farm, FAQ, Pet, Fodder])
