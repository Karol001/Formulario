from django.db import models


class Form(models.Model):
    Nombre = models.CharField(max_length=50, null=True)
    Cargoform = models.CharField(max_length=50, null=True)
    area = models.CharField(max_length=50, null=True)
    Correo = models.EmailField(null=True)
    bloque = models.CharField(max_length=50, null=True)
    Respuesta= models.CharField(max_length=100)
    item = models.CharField(max_length=100)


  

  
