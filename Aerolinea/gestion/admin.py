from django.contrib import admin
from .models import Avion, Vuelo, Pasajero, Asiento

# Register your models here.

admin.site.register(Avion)
admin.site.register(Vuelo)
admin.site.register(Pasajero)
admin.site.register(Asiento)
