from django.contrib import admin

from plants.models import PlantImage, Plants

# Register your models here.

admin.site.register([Plants, PlantImage])
