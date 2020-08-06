from django.db import models

# Create your models here.

class Cliente(models.Model):
	nombre 	= models.CharField(max_length =100)
	apellido	= models.CharField(max_length =100)
	correo	= models.EmailField()
	telefono	= models.IntegerField()

class Producto(models.Model):
	nombre		= models.CharField(max_length = 100)
	precio		= models.IntegerField()
	oferta	= models.BooleanField(default =False)
	precioOferta= models.IntegerField()

class DetalleVenta(models.Model):
	producto 	= models.ForeignKey(Producto, on_delete = models.CASCADE)
	cantidad	= models.IntegerField()

class Venta(models.Model):
	cliente 	= models.ForeignKey(Cliente, on_delete = models.CASCADE)
	detalleVenta= models.ForeignKey(DetalleVenta, on_delete = models.CASCADE)	
	fecha	= models.DateTimeField('data published')		

