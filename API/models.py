from django.db import models

# Create your models here.


class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=140)

    def __str__(self):
        return self.nombre

class Hamburguesa(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=140)
    imagen = models.URLField(max_length=100)
    ingredientes = models.ManyToManyField(Ingrediente)
    def __str__(self):
        return self.nombre