🛠️ Etapa 3: Creación e integración de la app gestión (estructura base)

🧩 Creación de la app de gestión
- Creamos una nueva app dentro del proyecto Django para manejar todas las funcionalidades administrativas del sistema (vuelos, aviones, pasajeros, etc.):
    python manage.py startapp gestion

🧠 Registro de la app en Django
- Agregamos 'gestion' a la lista de INSTALLED_APPS en el archivo settings.py:
    INSTALLED_APPS = [
        ...,

🛠️ Etapa 3: Integración inicial de la gestión

📁 Creación de la app gestion

- Creamos una nueva app llamada gestion, que se encargará de centralizar la gestión interna del sistema de la aerolínea (vuelos, pasajeros, aviones, etc.):
    python manage.py startapp gestion

🧠 Registro de la app en Django
- Agregamos 'gestion' al listado de INSTALLED_APPS en el archivo settings.py:
    INSTALLED_APPS = [
        ...
        'gestion',
    ]

🌐 Configuración de rutas

- En Aerolinea/urls.py, incluimos las URLs de la app gestión:

- En el archivo principal urls.py, enlazamos la app gestion:

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),

        path('', include('home.urls')),         # Página principal
        path('gestion/', include('gestion.urls')),  # Nueva sección de gestión
    ]

- Creamos el archivo gestion/urls.py con la estructura inicial:

        path('gestion/', include('gestion.urls')),  # Ruta hacia la app gestion
    ]

- Creamos el archivo gestion/urls.py y definimos una ruta básica:

    from django.urls import path
    from . import views

    urlpatterns = [

        # Las rutas de gestión se agregarán en las subetapas
    ]

✅ Verificación del funcionamiento
- Ejecutamos el servidor y verificamos que la ruta http://127.0.0.1:8000/gestion/ funciona correctamente (aunque aún no hay vistas definidas):
        path('', views.index, name='index'),

🖼️ Creación de vista y plantilla inicial
- En gestion/views.py, definimos una vista inicial de prueba:
    from django.shortcuts import render

    def index(request):
        return render(request, 'gestion/index.html')

- Creamos la carpeta de plantillas dentro de la app gestion:
    gestion/
    └── templates/
        └── gestion/
            └── index.html

- En index.html, escribimos un contenido de prueba:
    {% extends 'base.html' %}

    {% block contenido %}
    <h1>Bienvenido a la gestión de la Aerolínea</h1>
    {% endblock %}

✅ Verificación
- Iniciamos el servidor para comprobar que la app gestion está conectada correctamente:

    python manage.py runserver

- Y accedimos a: http://localhost:8000/gestion/

🗂️ Estructura actual del proyecto
    aerolinea-argentina/
    ├── Aerolinea/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── gestion/                  ← Nueva app
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── urls.py
    │   ├── views.py
    │   └── ...
    ├── gestion/
    │   ├── templates/
    │   │   └── gestion/
    │   │       └── index.html
    │   ├── views.py
    │   ├── urls.py
    │   └── ...
    ├── home/
    │   └── ...
    ├── manage.py
    └── requirements.txt
    └── ...

✍️ Autor
- Agustín Alejandro Fasano