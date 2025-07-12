🛠️ Etapa 3/pasajeros: Creación e integración de la app gestión (pasajeros)

🧩 Creación de la sección gestión de pasajeros
- Agregamos la funcionalidad dentro de la app gestion del proyecto Django, para manejar todo lo relacionado a los pasajeros.

🧠 Registro del modelo en el admin
- Registramos el modelo Pasajero en el archivo admin.py:
    from .models import Pasajero
    admin.site.register(Pasajero)

🌐 Configuración de rutas
- En el archivo gestion/urls.py, agregamos las rutas específicas para la gestión de pasajeros:
    urlpatterns += [
        path('pasajeros/', views.lista_pasajeros, name='lista_pasajeros'),
        path('pasajeros/agregar/', views.agregar_pasajero, name='agregar_pasajero'),
        path('pasajeros/editar/<int:id>/', views.editar_pasajero, name='editar_pasajero'),
        path('pasajeros/eliminar/<int:id>/', views.eliminar_pasajero, name='eliminar_pasajero'),
    ]

🖼️ Creación de vistas y plantillas
- Definimos las vistas en gestion/views.py:
    def lista_pasajeros(request): ...
    def agregar_pasajero(request): ...
    def editar_pasajero(request, id): ...
    def eliminar_pasajero(request, id): ...

- Creamos las plantillas HTML en:
    gestion/
    └── templates/
        └── pasajeros/
            ├── lista.html
            ├── formulario.html
            └── eliminar.html

- El formulario usa el PasajeroForm definido en forms.py, con campos como:
    1. nombre
    2. documento
    3. tipo_documento (con combo box)
    4. email
    5. teléfono
    6. fecha de nacimiento

✅ Verificación del funcionamiento
- Ejecutamos el servidor para probar:
    python manage.py runserver

- Accedemos a:
    📍 http://localhost:8000/pasajeros/
    📍 http://localhost:8000/pasajeros/agregar/
    📍 http://localhost:8000/pasajeros/editar/1/

🗂️ Estructura actual del proyecto (resumida)
    aerolinea-argentina/
    ├── gestion/
    │   ├── admin.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── urls.py
    │   ├── views.py
    │   └── templates/
    │       └── pasajeros/
    │           ├── lista.html
    │           ├── formulario.html
    │           └── eliminar.html
    ├── Aerolinea/
    │   └── urls.py
    ├── manage.py
    └── ...

✍️ Autor
- Agustín Alejandro Fasano