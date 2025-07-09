🛠️ Etapa 3/vuelos: Creación e integración de la app gestión (vuelos)

🧩 Creación de la app gestión de vuelos
- Creamos una nueva app dentro del proyecto Django para manejar todas las funcionalidades relacionadas con la gestión de vuelos:
    python manage.py startapp vuelos

🧠 Registro de la app en Django
- Agregamos 'vuelos' a la lista de INSTALLED_APPS en el archivo settings.py:
    INSTALLED_APPS = [
        ...
        'vuelos',
    ]

🌐 Configuración de rutas
- En el archivo Aerolinea/urls.py, incluimos las URLs de la app vuelos:
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('home.urls')),         # Página principal
        path('vuelos/', include('vuelos.urls')),  # Nueva sección de vuelos
    ]

- Creamos el archivo vuelos/urls.py con la estructura inicial:
    from django.urls import path
    from . import views

    urlpatterns = [
        # Las rutas de gestión de vuelos se agregarán en las subetapas
    ]

- Definimos una ruta básica en vuelos/urls.py:

    urlpatterns = [
        path('', views.lista_vuelos, name='lista_vuelos'),
    ]
✅ Verificación del funcionamiento
- Ejecutamos el servidor y verificamos que la ruta http://127.0.0.1:8000/vuelos/ funciona correctamente (aunque aún no hay vistas definidas):
    python manage.py runserver

🖼️ Creación de vista y plantilla inicial
- En vuelos/views.py, definimos una vista inicial de prueba:

    from django.shortcuts import render

    def lista_vuelos(request):
        return render(request, 'vuelos/lista.html')

- Creamos la carpeta de plantillas dentro de la app vuelos:
    vuelos/
    └── templates/
        └── vuelos/
            └── lista.html

- En lista.html, escribimos un contenido de prueba:
    {% extends 'base.html' %}

    {% block contenido %}
        <h1>Bienvenido a la gestión de vuelos</h1>
    {% endblock %}

✅ Verificación
- Iniciamos el servidor para comprobar que la app vuelos está conectada correctamente:
    python manage.py runserver

- Accedemos a: http://localhost:8000/vuelos/

🗂️ Estructura actual del proyecto
    aerolinea-argentina/
    ├── Aerolinea/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── vuelos/                   ← Nueva app
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── urls.py
    │   ├── views.py
    │   └── ...
    ├── vuelos/
    │   ├── templates/
    │   │   └── vuelos/
    │   │       └── lista.html
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