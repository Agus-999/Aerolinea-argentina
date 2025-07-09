🛠️ Etapa 3/aviones: Creación e integración de la app gestión (aviones)

🧩 Creación de la app gestión de aviones
- Creamos una nueva app dentro del proyecto Django para manejar todas las funcionalidades relacionadas con la gestión de aviones:
    python manage.py startapp aviones

🧠 Registro de la app en Django
- Agregamos 'aviones' a la lista de INSTALLED_APPS en el archivo settings.py:
    INSTALLED_APPS = [
        ...
        'aviones',
    ]

🌐 Configuración de rutas
- En el archivo Aerolinea/urls.py, incluimos las URLs de la app aviones:
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('home.urls')),         # Página principal
        path('aviones/', include('aviones.urls')),  # Nueva sección de aviones
    ]

- Creamos el archivo aviones/urls.py con la estructura inicial:
    from django.urls import path
    from . import views

    urlpatterns = [
        # Las rutas de gestión de aviones se agregarán en las subetapas
    ]

- Definimos una ruta básica en aviones/urls.py:
    urlpatterns = [
        path('', views.index, name='index'),
    ]

✅ Verificación del funcionamiento
- Ejecutamos el servidor y verificamos que la ruta http://127.0.0.1:8000/aviones/ funciona correctamente (aunque aún no hay vistas definidas):
    python manage.py runserver

🖼️ Creación de vista y plantilla inicial
- En aviones/views.py, definimos una vista inicial de prueba:
    from django.shortcuts import render

    def index(request):
        return render(request, 'aviones/index.html')

- Creamos la carpeta de plantillas dentro de la app aviones:
    aviones/
    └── templates/
        └── aviones/
            └── index.html

- En index.html, escribimos un contenido de prueba:
    {% extends 'base.html' %}

    {% block contenido %}
        <h1>Bienvenido a la gestión de aviones</h1>
    {% endblock %}

✅ Verificación
- Iniciamos el servidor para comprobar que la app aviones está conectada correctamente:
    python manage.py runserver

- Accedemos a: http://localhost:8000/aviones/

🗂️ Estructura actual del proyecto
    aerolinea-argentina/
    ├── Aerolinea/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── aviones/                   ← Nueva app
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── urls.py
    │   ├── views.py
    │   └── ...
    ├── aviones/
    │   ├── templates/
    │   │   └── aviones/
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