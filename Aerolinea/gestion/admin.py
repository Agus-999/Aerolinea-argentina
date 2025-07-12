from django.contrib import admin
from .models import Avion, Vuelo, Pasajero

# Register your models here.

admin.site.register(Avion)
admin.site.register(Vuelo)
admin.site.register(Pasajero)