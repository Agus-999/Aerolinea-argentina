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

class Asiento(models.Model):
    avion = models.ForeignKey('gestion.Avion', on_delete=models.CASCADE)  # identificación de aeronave
    numero = models.CharField(max_length=10)  # número AZ
    fila = models.PositiveIntegerField()      # fila
    columna = models.CharField(max_length=5)  # columna AZ
    estado = models.CharField(max_length=20, default='Disponible')  # estado (ej. Disponible, Ocupado)

    def __str__(self):
        return f"Asiento {self.numero} ({self.fila}{self.columna}) - {self.estado}"

class Reserva(models.Model):
    ESTADOS = [
        ('Reservado', 'Reservado'),
        ('Cancelado', 'Cancelado'),
        ('Confirmado', 'Confirmado'),
    ]

    vuelo = models.ForeignKey('gestion.Vuelo', on_delete=models.CASCADE)  # Relacionado con Vuelo
    pasajero = models.ForeignKey('gestion.Pasajero', on_delete=models.CASCADE)  # Relacionado con Pasajero
    asiento = models.OneToOneField('gestion.Asiento', on_delete=models.CASCADE)  # Relacionado con Asiento
    estado = models.CharField(max_length=20, choices=ESTADOS)  # Estado de la reserva
    fecha_reserva = models.DateTimeField(auto_now_add=True)  # Fecha en que se hace la reserva
    precio = models.DecimalField(max_digits=8, decimal_places=2)  # Precio de la reserva
    codigo_reserva = models.CharField(max_length=10, unique=True)  # Código único de reserva

    def __str__(self):
        return f"Reserva {self.codigo_reserva} - {self.pasajero.nombre} - {self.vuelo.origen} → {self.vuelo.destino}"

class Boleto(models.Model):
    reserva = models.OneToOneField('gestion.Reserva', on_delete=models.CASCADE)
    codigo_barra = models.CharField(max_length=100)
    fecha_emision = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"Boleto {self.codigo_barra} - {self.estado}"