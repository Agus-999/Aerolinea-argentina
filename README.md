🛫 Etapa 1: Creación del proyecto y conexión con base de datos

1. 🧱 Creación del entorno virtual
    Creamos y activamos un entorno virtual para aislar dependencias:

        python -m venv venv
        venv\Scripts\activate  # En Windows

2. ⚙️ Instalación de Django
    Instalamos Django dentro del entorno virtual:

        pip install django

3. 📁 Creación del proyecto base
    Ejecutamos el siguiente comando para crear el proyecto Django (evitamos guiones que no son válidos):

        django-admin startproject aerolinea_voladora .

4. 🗄️ Conexión con la base de datos existente
    Ya contábamos con una base de datos SQLite previamente creada, llamada:

        aerolineas_voladoras

    La colocamos en la raíz del proyecto (junto a manage.py), y luego configuramos el archivo settings.py así:

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / "aerolineas_voladoras.sqlite3",
            }
        }
5. ✅ Verificación del proyecto
    Aplicamos las migraciones iniciales de Django para asegurarnos que todo funciona:

        python manage.py migrate

📁 Estructura actual del proyecto
    aerolinea_voladora/
    ├── aerolinea_voladora/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── aerolineas_voladoras.sqlite3
    ├── manage.py
    ├── requirements.txt
    └── venv/

✍️ Autor
- Agustín Alejandro Fasano