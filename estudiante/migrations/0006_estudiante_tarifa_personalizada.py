# Generated by Django 5.1.2 on 2024-12-12 15:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0005_alter_estudiante_seccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='tarifa_personalizada',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]