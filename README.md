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
- En el archivo principal urls.py, enlazamos la app gestion:
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('gestion/', include('gestion.urls')),  # Ruta hacia la app gestion
    ]

- Creamos el archivo gestion/urls.py y definimos una ruta básica:
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]

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
    └── ...

✍️ Autor
- Agustín Alejandro Fasano