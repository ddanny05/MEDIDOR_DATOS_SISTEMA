from django.db import models

# Create your models here.
class Datos_personales(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10)
    peso = models.FloatField(help_text='ingresa el valor en libras')
    altura = models.FloatField(help_text='ingresa el valor en metros')
    estado_civil = models.CharField (max_length=30)
    nacionalidad = models.CharField(max_length=30)

    def __str__(self):
        return self.cedula
    
