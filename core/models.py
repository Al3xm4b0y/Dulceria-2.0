from django.db import models

# Create your models here.

class Producto (models.Model):
    codigo = models.CharField(max_length= 4, primary_key= True)
    detalle = models.CharField(max_length= 300)
    precio = models.IntegerField()
    stock = models.IntegerField()
    oferta = models.BooleanField()
    imagen = models.CharField(max_length=200) # permite agregar la ruta de la imagen