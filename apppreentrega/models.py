from django.db import models

# Create your models here.
class Client(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField()
    
class ClienteAsilo(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30)
    fecha_ingreso = models.DateField()
    
class ClienteTps(models.Model):
    social = models.IntegerField()
    pais = models.CharField(max_length=30)
    pasaporte =models.CharField(max_length=30)
    fecha_ingreso = models.DateField()