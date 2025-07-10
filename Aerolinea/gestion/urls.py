from django.urls import path
from . import views

urlpatterns = [
    #* AVIONES
    path('aviones/', views.lista_aviones, name='lista_aviones'),
    path('aviones/agregar/', views.agregar_avion, name='agregar_avion'),
    path('aviones/editar/<int:id>/', views.editar_avion, name='editar_avion'),
    path('aviones/eliminar/<int:id>/', views.eliminar_avion, name='eliminar_avion'),

    #* VUELOS
    path('vuelos/', views.lista_vuelos, name='lista_vuelos'),
    path('vuelos/agregar/', views.agregar_vuelo, name='agregar_vuelo'),
    path('vuelos/editar/<int:id>/', views.editar_vuelo, name='editar_vuelo'),
    path('vuelos/eliminar/<int:id>/', views.eliminar_vuelo, name='eliminar_vuelo'),

    #* PASAJEROS
    path('pasajeros/', views.lista_pasajeros, name='lista_pasajeros'),
    path('pasajeros/agregar/', views.agregar_pasajero, name='agregar_pasajero'),
    path('pasajeros/editar/<int:id>/', views.editar_pasajero, name='editar_pasajero'),
    path('pasajeros/eliminar/<int:id>/', views.eliminar_pasajero, name='eliminar_pasajero'),

    #* ASIENTOS
    path('asientos/', views.lista_asientos, name='lista_asientos'),
    path('asientos/agregar/', views.agregar_asiento, name='agregar_asiento'),
    path('asientos/editar/<int:id>/', views.editar_asiento, name='editar_asiento'),
    path('asientos/eliminar/<int:id>/', views.eliminar_asiento, name='eliminar_asiento'),

]
