# Generated by Django 5.2.3 on 2025-07-09 20:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origen', models.CharField(max_length=100)),
                ('destino', models.CharField(max_length=100)),
                ('fecha_salida', models.CharField(max_length=100)),
                ('fecha_llegada', models.CharField(max_length=100)),
                ('duracion', models.CharField(max_length=100)),
                ('estado', models.CharField(default='Programado', max_length=50)),
                ('precio_base', models.FloatField(blank=True, null=True)),
                ('avion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.avion')),
            ],
        ),
    ]
