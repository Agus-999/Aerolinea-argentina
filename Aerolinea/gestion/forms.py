# gestion/forms.py

from django import forms
from .models import Avion, Vuelo

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