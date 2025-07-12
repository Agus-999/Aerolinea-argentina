🎟️ Etapa 3/boletos: CRUD de Boletos

🧰 En esta etapa implementamos el CRUD completo de Boletos, permitiendo emitir y gestionar los boletos que se generan a partir de una reserva confirmada. Cada boleto contiene información importante como la reserva asociada, código de barra, fecha de emisión y estado. Esta funcionalidad es clave para el control final del viaje de un pasajero.

🧱 Modelo de Boleto  
- Definimos el modelo `Boleto` en `gestion/models.py` con los siguientes campos:
    class Boleto(models.Model):
        reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
        codigo_barra = models.CharField(max_length=50)
        fecha_emision = models.DateField()
        estado = models.CharField(max_length=20, default='Emitido')

- Registramos el modelo en el admin:
    admin.site.register(Boleto)

- Aplicamos las migraciones:
    python manage.py makemigrations gestion
    python manage.py migrate

🧾 Formulario personalizado
- Creamos el formulario BoletoForm en gestion/forms.py con widgets mejorados para fechas y entradas:
    class BoletoForm(forms.ModelForm):
        ESTADOS = [
            ('Emitido', 'Emitido'),
            ('Anulado', 'Anulado'),
            ('Usado', 'Usado'),
        ]
        estado = forms.ChoiceField(choices=ESTADOS, widget=forms.Select(attrs={'class': 'form-control'}))

        class Meta:
            model = Boleto
            fields = '__all__'
            widgets = {
                'fecha_emision': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                'codigo_barra': forms.TextInput(attrs={'class': 'form-control'}),
                'reserva': forms.Select(attrs={'class': 'form-control'}),
            }

👁️‍🗨️ Vistas implementadas
- Creamos las vistas del CRUD de Boletos en gestion/views.py:

Vista	            | Descripción
--------------------+-----------------------------------------
lista_boletos	    | Lista todos los boletos emitidos
agregar_boleto	    | Formulario para emitir un nuevo boleto
editar_boleto	    | Modifica un boleto existente
eliminar_boleto	    | Confirma y elimina un boleto específico

🔁 Configuración de rutas
- En gestion/urls.py agregamos las siguientes rutas:
    path('boletos/', views.lista_boletos, name='lista_boletos'),
    path('boletos/agregar/', views.agregar_boleto, name='agregar_boleto'),
    path('boletos/editar/<int:id>/', views.editar_boleto, name='editar_boleto'),
    path('boletos/eliminar/<int:id>/', views.eliminar_boleto, name='eliminar_boleto'),

🖼️ Templates utilizados
- Carpeta: gestion/templates/boletos/

Archivo	        | Descripción
----------------+------------------------------------------
lista.html	    | Lista de boletos con datos y acciones
formulario.html	| Formulario para agregar o editar boletos
eliminar.html	| Confirmación para eliminar un boleto

🌐 Navegación general del sitio
- Desde el menú en base.html se puede acceder a:
    🏠 Inicio
    ✈ Aviones
    🛫 Vuelos
    💺 Asientos
    🎫 Reservas
    🎟️ Boletos

✅ Verificación del funcionamiento
- Ejecutamos el servidor:
    python manage.py runserver

- En http://127.0.0.1:8000/gestion/boletos/ se puede:
    - Ver todos los boletos emitidos
    - Agregar nuevos boletos
    - Editar y eliminar los existentes

🗂️ Estructura del proyecto actual
    aerolinea-argentina/
    ├── aerolinea/
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
    │   │   └── boletos/
    │   │       ├── lista.html
    │   │       ├── formulario.html
    │   │       └── eliminar.html
    │   └── ...
    ├── manage.py
    └── venv/

✍️ Autor
- Agustín Alejandro Fasano
