from django.db import models

# Create your models here.

class Avion(models.Model):
    modelo = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    filas = models.PositiveIntegerField()
    columnas = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.modelo} - {self.capacidad} pasajeros"

class Vuelo(models.Model):
    avion = models.ForeignKey(Avion, on_delete=models.CASCADE)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha_salida = models.CharField(max_length=100)
    fecha_llegada = models.CharField(max_length=100)
    duracion = models.CharField(max_length=100)
    estado = models.CharField(max_length=50, default='Programado')
    precio_base = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.origen} → {self.destino} ({self.fecha_salida})"

class Pasajero(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=50, unique=True)
    tipo_documento = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.CharField(max_length=30)
    fecha_nac = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} ({self.documento})"
