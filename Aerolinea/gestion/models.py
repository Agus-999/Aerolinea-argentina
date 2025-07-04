from django.db import models

# Create your models here.

class Avion(models.Model):
    modelo = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    filas = models.PositiveIntegerField()
    columnas = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.modelo} - {self.capacidad} pasajeros"
