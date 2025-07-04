🧰 Etapa 3: CRUD de Aviones
✈️ En esta etapa comenzamos con la gestión de datos reales dentro del sistema, implementando el CRUD completo de Aviones (crear, leer, actualizar y eliminar) usando vistas propias, formularios personalizados y plantillas web.

🧩 Creación de la app gestion
- Creamos una nueva app para agrupar todas las gestiones administrativas:

    python manage.py startapp gestion

🧠 Registro de la app en Django
- Agregamos 'gestion' a la lista de apps instaladas en settings.py:

    INSTALLED_APPS = [
        ...
        'home',
        'gestion',
    ]

🔁 Configuración de rutas
- En aerolinea_voladora/urls.py, conectamos la app gestion:

    from django.urls import path, include

    urlpatterns = [
        ...
        path('gestion/', include('gestion.urls')),
    ]

- En gestion/urls.py, definimos las rutas para el CRUD:

    from django.urls import path
    from . import views

    urlpatterns = [
        path('aviones/', views.lista_aviones, name='lista_aviones'),
        path('aviones/agregar/', views.agregar_avion, name='agregar_avion'),
        path('aviones/editar/<int:id>/', views.editar_avion, name='editar_avion'),
        path('aviones/eliminar/<int:id>/', views.eliminar_avion, name='eliminar_avion'),
    ]
🧱 Modelo de Avión
- Definimos el modelo Avion en gestion/models.py:

    class Avion(models.Model):
        modelo = models.CharField(max_length=100)
        capacidad = models.PositiveIntegerField()
        filas = models.PositiveIntegerField()
        columnas = models.PositiveIntegerField()

- Registramos el modelo en el admin:
    
    admin.site.register(Avion)
        Aplicamos las migraciones:
            python manage.py makemigrations gestion
            python manage.py migrate

🧾 Formulario personalizado
- Creamos el formulario AvionForm en gestion/forms.py para mejorar la experiencia de carga de datos con labels y clases CSS.

👁️‍🗨️ Vistas implementadas
- Creamos 4 vistas en gestion/views.py:

        Vista	       | Descripción
        ---------------+----------------------------------------
        lista_aviones  | Muestra todos los aviones cargados
        agregar_avion  | Permite registrar un nuevo avión
        editar_avion   | Permite modificar un avión existente
        eliminar_avion | Confirma y elimina un avión específico

🖼️ Templates utilizados
- Carpeta: gestion/templates/aviones/

        Archivo	        | Descripción
        ----------------+--------------------------------------
        lista.html	    | Lista de aviones con botones CRUD
        formulario.html	| Formulario para agregar o editar
        eliminar.html	| Página de confirmación para eliminar

🌐 Navegación general del sitio
- Agregamos un menú de navegación dentro de base.html para poder acceder fácilmente a:

        🏠 Inicio

        ✈ Aviones

✅ Verificación del funcionamiento
- Ejecutamos el servidor y comprobamos que:
    python manage.py runserver
    
    En http://127.0.0.1:8000/gestion/aviones/ se pueden:

       - Ver los aviones

       - Agregar nuevos

       - Editar o eliminar desde la tabla

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
    │   │   └── gestion/
    │   │       └── aviones/
    │   │           ├── lista.html
    │   │           ├── formulario.html
    │   │           └── eliminar.html
    │   └── ...
    ├── manage.py
    └── venv/

✍️ Autor
- Agustín Alejandro Fasano