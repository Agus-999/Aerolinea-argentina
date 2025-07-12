# gestion/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Avion, Vuelo, Pasajero, Asiento, Reserva, Boleto
from .forms import AvionForm, VueloForm, PasajeroForm, AsientoForm, ReservaForm, BoletoForm

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

#* PASAJEROS
def lista_pasajeros(request):
    pasajeros = Pasajero.objects.all()
    return render(request, 'pasajeros/lista.html', {'pasajeros': pasajeros})

def agregar_pasajero(request):
    if request.method == 'POST':
        form = PasajeroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pasajeros')
    else:
        form = PasajeroForm()
    return render(request, 'pasajeros/formulario.html', {'form': form, 'accion': 'Agregar Pasajero'})

def editar_pasajero(request, id):
    pasajero = get_object_or_404(Pasajero, pk=id)
    if request.method == 'POST':
        form = PasajeroForm(request.POST, instance=pasajero)
        if form.is_valid():
            form.save()
            return redirect('lista_pasajeros')
    else:
        form = PasajeroForm(instance=pasajero)
    return render(request, 'pasajeros/formulario.html', {'form': form, 'accion': 'Editar Pasajero'})

def eliminar_pasajero(request, id):
    pasajero = get_object_or_404(Pasajero, pk=id)
    if request.method == 'POST':
        pasajero.delete()
        return redirect('lista_pasajeros')
    return render(request, 'pasajeros/eliminar.html', {'pasajero': pasajero})

#* ASIENTOS
def lista_asientos(request):
    asientos = Asiento.objects.all()
    return render(request, 'asientos/lista.html', {'asientos': asientos})

def agregar_asiento(request):
    if request.method == 'POST':
        form = AsientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_asientos')
    else:
        form = AsientoForm()
    return render(request, 'asientos/formulario.html', {'form': form, 'accion': 'Agregar Asiento'})

def editar_asiento(request, id):
    asiento = get_object_or_404(Asiento, pk=id)
    if request.method == 'POST':
        form = AsientoForm(request.POST, instance=asiento)
        if form.is_valid():
            form.save()
            return redirect('lista_asientos')
    else:
        form = AsientoForm(instance=asiento)
    return render(request, 'asientos/formulario.html', {'form': form, 'accion': 'Editar Asiento'})

def eliminar_asiento(request, id):
    asiento = get_object_or_404(Asiento, pk=id)
    if request.method == 'POST':
        asiento.delete()
        return redirect('lista_asientos')
    return render(request, 'asientos/eliminar.html', {'asiento': asiento})

#* RESERVAS
# Vista para listar todas las reservas
def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/lista.html', {'reservas': reservas})

# Vista para agregar una nueva reserva
def agregar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm()
    return render(request, 'reservas/formulario.html', {'form': form, 'accion': 'Agregar Reserva'})

# Vista para editar una reserva
def editar_reserva(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reservas/formulario.html', {'form': form, 'accion': 'Editar Reserva'})

# Vista para eliminar una reserva
def eliminar_reserva(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    if request.method == 'POST':
        reserva.delete()
        return redirect('lista_reservas')
    return render(request, 'reservas/eliminar.html', {'reserva': reserva})

#* BOLETOS
# Vista para listar boletos
def lista_boletos(request):
    boletos = Boleto.objects.all()
    return render(request, 'boletos/lista.html', {'boletos': boletos})

# Agregar
def agregar_boleto(request):
    form = BoletoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_boletos')
    return render(request, 'boletos/formulario.html', {'form': form, 'accion': 'Agregar Boleto'})

# Editar
def editar_boleto(request, id):
    boleto = get_object_or_404(Boleto, pk=id)
    form = BoletoForm(request.POST or None, instance=boleto)
    if form.is_valid():
        form.save()
        return redirect('lista_boletos')
    return render(request, 'boletos/formulario.html', {'form': form, 'accion': 'Editar Boleto'})

# Eliminar
def eliminar_boleto(request, id):
    boleto = get_object_or_404(Boleto, pk=id)
    if request.method == 'POST':
        boleto.delete()
        return redirect('lista_boletos')
    return render(request, 'boletos/eliminar.html', {'boleto': boleto})
