# gestion/forms.py

from django import forms
from .models import Avion

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
