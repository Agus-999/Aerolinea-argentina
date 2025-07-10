💺 Etapa 3/asientos: CRUD de Asientos

🧰 En esta etapa implementamos el CRUD completo de Asientos, permitiendo gestionar todos los asientos de cada avión: creación, edición, eliminación y listado. Esta funcionalidad es clave para luego asignar correctamente asientos a las reservas.

🧱 Modelo de Asiento  
- Definimos el modelo `Asiento` en `vuelos/models.py` con los siguientes campos:
    class Asiento(models.Model):
        avion = models.ForeignKey(Avion, on_delete=models.CASCADE)
        numero = models.CharField(max_length=5)
        fila = models.PositiveIntegerField()
        columna = models.CharField(max_length=2)
        estado = models.CharField(max_length=20, default='Disponible')

- Registramos el modelo en el admin:
    admin.site.register(Asiento)

- Aplicamos las migraciones:
    python manage.py makemigrations vuelos
    python manage.py migrate

🧾 Formulario personalizado
- Creamos el formulario AsientoForm en gestion/forms.py con estilos y etiquetas amigables:
    class AsientoForm(forms.ModelForm):
        ESTADOS = [
            ('Disponible', 'Disponible'),
            ('Ocupado', 'Ocupado'),
            ('Reservado', 'Reservado'),
        ]
        estado = forms.ChoiceField(choices=ESTADOS, widget=forms.Select(attrs={'class': 'form-control'}))

👁️‍🗨️ Vistas implementadas
- Creamos las vistas del CRUD de Asientos en gestion/views.py:

    Vista	            | Descripción
    --------------------+------------------------------------------
    lista_asientos	    | Lista todos los asientos cargados
    agregar_asiento	    | Formulario para registrar un asiento
    editar_asiento	    | Modifica un asiento existente
    eliminar_asiento	| Confirma y elimina un asiento específico

🔁 Configuración de rutas
- En gestion/urls.py agregamos las siguientes rutas:
    path('asientos/', views.lista_asientos, name='lista_asientos'),
    path('asientos/agregar/', views.agregar_asiento, name='agregar_asiento'),
    path('asientos/editar/<int:id>/', views.editar_asiento, name='editar_asiento'),
    path('asientos/eliminar/<int:id>/', views.eliminar_asiento, name='eliminar_asiento'),

🖼️ Templates utilizados
- Carpeta: gestion/templates/asientos/

    Archivo	        | Descripción
    ----------------+------------------------------------------
    lista.html	    | Lista de asientos con botones de acción
    formulario.html	| Formulario para agregar o editar asientos
    eliminar.html	| Confirmación para eliminar un asiento

🌐 Navegación general del sitio
- Desde el menú en base.html se puede acceder a:
    🏠 Inicio
    ✈ Aviones
    🛫 Vuelos
    💺 Asientos

✅ Verificación del funcionamiento
- Ejecutamos el servidor:
    python manage.py runserver

- En http://127.0.0.1:8000/gestion/asientos/ se puede:

    Ver los asientos cargados
    Agregar nuevos asientos
    Editar y eliminar los existentes

🗂️ Estructura del proyecto actual
    aerolinea_voladora/
    ├── aerolinea_voladora/
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    ├── home/
    │   ├── templates/
    │   │   └── base.html
    │   └── ...
    ├── gestion/
    │   ├── forms.py
    │   ├── models.py
    │   ├── urls.py
    │   ├── views.py
    │   ├── templates/
    │   │   └── asientos/
    │   │       ├── lista.html
    │   │       ├── formulario.html
    │   │       └── eliminar.html
    │   └── ...
    ├── vuelos/
    │   ├── models.py
    │   └── ...
    ├── manage.py
    └── venv/

✍️ Autor
- Agustín Alejandro Fasano