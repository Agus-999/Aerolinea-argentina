from django.urls import path
from . import views

urlpatterns = [
    path('aviones/', views.lista_aviones, name='lista_aviones'),
    path('aviones/agregar/', views.agregar_avion, name='agregar_avion'),
    path('aviones/editar/<int:id>/', views.editar_avion, name='editar_avion'),
    path('aviones/eliminar/<int:id>/', views.eliminar_avion, name='eliminar_avion'),
]
