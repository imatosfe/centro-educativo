# Generated by Django 5.1.2 on 2024-11-27 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secciones', to='grado.grado')),
            ],
        ),
    ]
