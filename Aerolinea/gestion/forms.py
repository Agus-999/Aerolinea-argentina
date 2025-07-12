# gestion/forms.py

from django import forms
from .models import Avion, Vuelo, Pasajero, Asiento, Reserva, Boleto

class AvionForm(forms.ModelForm):
    class Meta:
        model = Avion
        fields = ['modelo', 'capacidad', 'filas', 'columnas']
        labels = {
            'modelo': 'Modelo del avión',
            'capacidad': 'Capacidad total',
            'filas': 'Cantidad de filas',
            'columnas': 'Cantidad de columnas'
        }
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'filas': forms.NumberInput(attrs={'class': 'form-control'}),
            'columnas': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class VueloForm(forms.ModelForm):
    ESTADOS = [
        ('Programado', 'Programado'),
        ('En vuelo', 'En vuelo'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    ]

    estado = forms.ChoiceField(choices=ESTADOS, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Vuelo
        fields = ['avion', 'origen', 'destino', 'fecha_salida', 'fecha_llegada', 'duracion', 'estado', 'precio_base']
        labels = {
            'avion': 'Avión asignado',
            'origen': 'Origen',
            'destino': 'Destino',
            'fecha_salida': 'Fecha de salida',
            'fecha_llegada': 'Fecha de llegada',
            'duracion': 'Duración',
            'estado': 'Estado',
            'precio_base': 'Precio base',
        }
        widgets = {
            'avion': forms.Select(attrs={'class': 'form-control'}),
            'origen': forms.TextInput(attrs={'class': 'form-control'}),
            'destino': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_salida': forms.TextInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            }),
            'fecha_llegada': forms.TextInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            }),
            'duracion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 2h 15m'}),
            'precio_base': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PasajeroForm(forms.ModelForm):
    TIPO_DOC = [
        ('DNI', 'DNI'),
        ('Pasaporte', 'Pasaporte'),
        ('Otro', 'Otro')
    ]

    tipo_documento = forms.ChoiceField(
        choices=TIPO_DOC,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Pasajero
        fields = ['nombre', 'documento', 'tipo_documento', 'email', 'telefono', 'fecha_nac']
        labels = {
            'nombre': 'Nombre completo',
            'documento': 'Número de documento',
            'tipo_documento': 'Tipo de documento',
            'email': 'Correo electrónico',
            'telefono': 'Teléfono',
            'fecha_nac': 'Fecha de nacimiento',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nac': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AAAA'}),
        }

class AsientoForm(forms.ModelForm):
    ESTADOS = [
        ('Disponible', 'Disponible'),
        ('Ocupado', 'Ocupado'),
        ('Reservado', 'Reservado'),
    ]

    estado = forms.ChoiceField(
        choices=ESTADOS,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Asiento
        fields = ['avion', 'numero', 'fila', 'columna', 'estado']
        labels = {
            'avion': 'Avión',
            'numero': 'Número',
            'fila': 'Fila',
            'columna': 'Columna',
            'estado': 'Estado'
        }
        widgets = {
            'avion': forms.Select(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'fila': forms.NumberInput(attrs={'class': 'form-control'}),
            'columna': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['vuelo', 'pasajero', 'asiento', 'estado', 'precio']
        labels = {
            'vuelo': 'Vuelo',
            'pasajero': 'Pasajero',
            'asiento': 'Asiento',
            'estado': 'Estado de la Reserva',
            'precio': 'Precio',
        }
        widgets = {
            'vuelo': forms.Select(attrs={'class': 'form-control'}),
            'pasajero': forms.Select(attrs={'class': 'form-control'}),
            'asiento': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class BoletoForm(forms.ModelForm):
    ESTADOS = [
        ('Válido', 'Válido'),
        ('Usado', 'Usado'),
        ('Cancelado', 'Cancelado'),
    ]

    estado = forms.ChoiceField(choices=ESTADOS, widget=forms.Select(attrs={'class': 'form-control'}))
    fecha_emision = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label="Fecha de emisión"
    )
    codigo_barra = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: BOL123456789'
        }),
        label="Código de barras"
    )

    class Meta:
        model = Boleto
        fields = '__all__'
        widgets = {
            'reserva': forms.Select(attrs={'class': 'form-control'}),
        }