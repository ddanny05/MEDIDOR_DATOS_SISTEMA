# Generated by Django 5.1.3 on 2024-11-18 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datos_personales',
            fields=[
                ('cedula', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('peso', models.FloatField(help_text='ingresa el valor en libras')),
                ('altura', models.FloatField(help_text='ingresa el valor en metros')),
                ('estado_civil', models.CharField(max_length=30)),
                ('nacionalidad', models.CharField(max_length=30)),
            ],
        ),
    ]
