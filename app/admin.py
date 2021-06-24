from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Hotel, Ruta
# Register your models here.


class HotelAdmin(admin.ModelAdmin):
    list_display = ["nombre","ubicacion","precio"]

class RutaAdmin(admin.ModelAdmin):
    list_display = ["nombre"]

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Ruta)
