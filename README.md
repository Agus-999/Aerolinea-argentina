🎫 Etapa 3/reservas: CRUD de Reservas

🧰 En esta etapa implementamos el CRUD completo de Reservas, permitiendo registrar y gestionar las reservas de pasajeros para vuelos específicos, asociando asientos y generando un flujo claro de operaciones. Esta funcionalidad es clave para que el sistema de gestión de aerolínea esté completo y operativo.

🧱 Modelo de Reserva  
- Definimos el modelo `Reserva` en `gestion/models.py` con los siguientes campos:
    class Reserva(models.Model):
        vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)
        pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
        asiento = models.ForeignKey(Asiento, on_delete=models.CASCADE)
        estado = models.CharField(max_length=20, default='Reservado')
        fecha_reserva = models.DateField(auto_now_add=True)
        precio = models.FloatField()
        codigo_reserva = models.CharField(max_length=10, unique=True)

- Registramos el modelo en el admin:
    admin.site.register(Reserva)

- Aplicamos las migraciones:
    python manage.py makemigrations gestion
    python manage.py migrate

🧾 Formulario personalizado
- Creamos el formulario `ReservaForm` en `gestion/forms.py`:

    class ReservaForm(forms.ModelForm):
        class Meta:
            model = Reserva
            fields = '__all__'
            widgets = {
                'fecha_reserva': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                'estado': forms.Select(choices=[('Reservado', 'Reservado'), ('Cancelado', 'Cancelado')], attrs={'class': 'form-control'}),
                'precio': forms.NumberInput(attrs={'class': 'form-control'}),
                'codigo_reserva': forms.TextInput(attrs={'class': 'form-control'}),
            }

👁️‍🗨️ Vistas implementadas
- Creamos las vistas del CRUD de Reservas en `gestion/views.py`:

    | Vista              | Descripción                            |
    |--------------------|----------------------------------------|
    | lista_reservas     | Lista todas las reservas cargadas      |
    | agregar_reserva    | Formulario para registrar una reserva  |
    | editar_reserva     | Modifica una reserva existente         |
    | eliminar_reserva   | Confirma y elimina una reserva         |

🔁 Configuración de rutas
- En `gestion/urls.py` agregamos las siguientes rutas:

    path('reservas/', views.lista_reservas, name='lista_reservas'),
    path('reservas/agregar/', views.agregar_reserva, name='agregar_reserva'),
    path('reservas/editar/<int:id>/', views.editar_reserva, name='editar_reserva'),
    path('reservas/eliminar/<int:id>/', views.eliminar_reserva, name='eliminar_reserva'),
    ```

🖼️ Templates utilizados
- Carpeta: `gestion/templates/reservas/`

    | Archivo           | Descripción                                 |
    |-------------------|---------------------------------------------|
    | lista.html        | Lista de reservas con botones de acción     |
    | formulario.html   | Formulario para agregar o editar reservas   |
    | eliminar.html     | Confirmación para eliminar una reserva      |

🌐 Navegación general del sitio
- Desde el menú en `base.html` se puede acceder a:
    - 🏠 Inicio  
    - ✈ Aviones  
    - 🛫 Vuelos  
    - 💺 Asientos  
    - 🎫 Reservas  

✅ Verificación del funcionamiento
- Ejecutamos el servidor:
    ```bash
    python manage.py runserver
    ```

- En http://127.0.0.1:8000/gestion/reservas/ se puede:

    - Ver las reservas registradas  
    - Agregar nuevas reservas  
    - Editar y eliminar las existentes  

🗂️ Estructura del proyecto actual
    aerolinea-argentina/
    ├── aerolinea/
    │ ├── settings.py
    │ ├── urls.py
    │ └── ...
    ├── home/
    │ ├── templates/
    │ │ └── base.html
    │ └── ...
    ├── gestion/
    │ ├── forms.py
    │ ├── models.py
    │ ├── urls.py
    │ ├── views.py
    │ ├── templates/
    │ │ └── reservas/
    │ │ ├── lista.html
    │ │ ├── formulario.html
    │ │ └── eliminar.html
    │ └── ...
    ├── manage.py
    └── venv/

✍️ Autor  
- Agustín Alejandro Fasano