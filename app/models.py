from django.db import models

class Hotel(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=60)
    precio = models.IntegerField(null=False)
    descripcion = models.TextField()
    estrellas = models.IntegerField(null=True)
    imagen = models.ImageField(upload_to="hoteles",null=True)

    def __str__(self):
        return self.nombre

class Ruta(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="rutas", null=True)

    def __str__(self):
        return self.nombre