🏠 Etapa 2: Creación de la app home y estructura base de la web

🧩 Creación de la app principal (home)
- Creamos una nueva app dentro del proyecto Django para manejar la parte principal del sitio:

    python manage.py startapp home

🧠 Registro de la app en Django
- Agregamos 'home' a la lista de INSTALLED_APPS en el archivo settings.py:

    INSTALLED_APPS = [
        ...
        'home',
    ]

🌐 Configuración de rutas
- En aerolinea_voladora/urls.py, incluimos las URLs de la app home:

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('home.urls')),
    ]

- Creamos el archivo home/urls.py con la ruta base al inicio de la página:

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.inicio, name='inicio'),
    ]

🖼️ Creación de las vistas y plantillas

- En home/views.py, definimos la vista para la página inicial:

    from django.shortcuts import render

    def inicio(request):
        return render(request, 'inicio.html')
- Creamos una carpeta templates/ dentro de la app home:

    home/
    └── templates/
        ├── base.html
        └── inicio.html

- En base.html, definimos la estructura general del sitio:

    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Aerolínea Argentina</title>
    </head>
    <body>
        {% block contenido %}
        {% endblock %}
    </body>
    </html>

- En inicio.html, extendemos de la base y colocamos contenido inicial:

    {% extends 'base.html' %}

    {% block contenido %}
        <h1>Bienvenido a Aerolínea Argentina</h1>
    {% endblock %}

✅ Verificación del funcionamiento
- Ejecutamos el servidor y comprobamos que se visualiza la página inicial correctamente:

    python manage.py runserver

🗂️ Estructura actual del proyecto
    aerolinea_voladora/
    ├── aerolinea_voladora/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── home/
    │   ├── migrations/
    │   ├── templates/
    │   │   ├── base.html
    │   │   └── inicio.html
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── aerolineas_voladoras
    ├── manage.py
    ├── requirements.txt
    └── venv/

✍️ Autor
- Agustín Alejandro Fasano

