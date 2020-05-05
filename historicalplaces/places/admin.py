from django.contrib import admin

# Register your models here.
from places.models import Place, Rate

admin.site.register(Place)
admin.site.register(Rate)
