🛠️ Etapa 3: Creación e integración de la app gestión (estructura base)

🧩 Creación de la app de gestión
- Creamos una nueva app dentro del proyecto Django para manejar todas las funcionalidades administrativas del sistema (vuelos, aviones, pasajeros, etc.):
    python manage.py startapp gestion

🧠 Registro de la app en Django
- Agregamos 'gestion' a la lista de INSTALLED_APPS en el archivo settings.py:
    INSTALLED_APPS = [
        ...,
        'gestion',
    ]

🌐 Configuración de rutas
- En Aerolinea/urls.py, incluimos las URLs de la app gestión:
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('home.urls')),         # Página principal
        path('gestion/', include('gestion.urls')),  # Nueva sección de gestión
    ]

- Creamos el archivo gestion/urls.py con la estructura inicial:
    from django.urls import path
    from . import views

    urlpatterns = [
        # Las rutas de gestión se agregarán en las subetapas
    ]

✅ Verificación del funcionamiento
- Ejecutamos el servidor y verificamos que la ruta http://127.0.0.1:8000/gestion/ funciona correctamente (aunque aún no hay vistas definidas):
    python manage.py runserver

🗂️ Estructura actual del proyecto
    aerolinea-argentina/
    ├── Aerolinea/
    │   ├── __init__.py
    │   ├── asgi.py
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
    ├── home/
    │   └── ...
    ├── manage.py
    └── requirements.txt

✍️ Autor
- Agustín Alejandro Fasano