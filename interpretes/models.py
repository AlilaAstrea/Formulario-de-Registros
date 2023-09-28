from django.db import models

class Interprete(models.Model):
    nombre = models.TextField(max_length=50)
    genero = models.TextField(max_length=50)
    clasificacion = models.TextField(max_length=30)
    aparicion = models.DateField()
