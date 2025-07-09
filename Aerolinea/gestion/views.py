# gestion/views.py


# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Avion
from .forms import AvionForm

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

