# gestion/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Avion, Vuelo
from .forms import AvionForm, VueloForm

#* AVIONES

def lista_aviones(request):
    aviones = Avion.objects.all()
    return render(request, 'aviones/lista.html', {'aviones': aviones})

def agregar_avion(request):
    if request.method == 'POST':
        form = AvionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_aviones')
    else:
        form = AvionForm()
    return render(request, 'aviones/formulario.html', {'form': form, 'accion': 'Agregar Avión'})

def editar_avion(request, id):
    avion = get_object_or_404(Avion, pk=id)
    if request.method == 'POST':
        form = AvionForm(request.POST, instance=avion)
        if form.is_valid():
            form.save()
            return redirect('lista_aviones')
    else:
        form = AvionForm(instance=avion)
    return render(request, 'aviones/formulario.html', {'form': form, 'accion': 'Editar Avión'})

def eliminar_avion(request, id):
    avion = get_object_or_404(Avion, pk=id)
    if request.method == 'POST':
        avion.delete()
        return redirect('lista_aviones')
    return render(request, 'aviones/eliminar.html', {'avion': avion})


#* VUELOS

def lista_vuelos(request):
    vuelos = Vuelo.objects.all()
    return render(request, 'vuelos/lista.html', {'vuelos': vuelos})

def agregar_vuelo(request):
    if request.method == 'POST':
        form = VueloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_vuelos')
    else:
        form = VueloForm()
    return render(request, 'vuelos/formulario.html', {'form': form, 'accion': 'Agregar Vuelo'})

def editar_vuelo(request, id):
    vuelo = get_object_or_404(Vuelo, pk=id)
    if request.method == 'POST':
        form = VueloForm(request.POST, instance=vuelo)
        if form.is_valid():
            form.save()
            return redirect('lista_vuelos')
    else:
        form = VueloForm(instance=vuelo)
    return render(request, 'vuelos/formulario.html', {'form': form, 'accion': 'Editar Vuelo'})

def eliminar_vuelo(request, id):
    vuelo = get_object_or_404(Vuelo, pk=id)
    if request.method == 'POST':
        vuelo.delete()
        return redirect('lista_vuelos')
    return render(request, 'vuelos/eliminar.html', {'vuelo': vuelo})