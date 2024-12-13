from django.db import models

class Padre(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Hijo(models.Model):
    padre = models.ForeignKey(Padre, on_delete=models.CASCADE, related_name='hijos')
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"


# En tu archivo models.py de la app existente
from django.db import models

class Zoologico(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Animal(models.Model):
    zoologico = models.ForeignKey(Zoologico, on_delete=models.CASCADE, related_name="animales")
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    edad = models.IntegerField()
    estado_salud = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"
