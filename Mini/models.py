from django.db import models

# Create your models here.

class Cliente(models.Model):
	user			= models.CharField(max_length=50)
	password		= models.CharField(('password'), max_length=128)
	nombre 			= models.CharField(max_length =100)
	apellido		= models.CharField(max_length =100)
	correo			= models.EmailField()
	telefono		= models.IntegerField()
	direccion		= models.CharField(max_length=100)
	admin			= models.BooleanField(default= False)
	
class Producto(models.Model):
	nombre			= models.CharField(max_length = 100)
	descripcion		= models.CharField(max_length=200)
	imagen			= models.ImageField(upload_to='pics')
	precio			= models.DecimalField(max_digits=10, decimal_places=2)
	oferta			= models.BooleanField(default =False)
	precioOferta	= models.DecimalField(max_digits=10, decimal_places=2)
	fechaVencimineto= models.DateField()
	stock			= models.IntegerField()

class DetalleVenta(models.Model):
	producto 		= models.ForeignKey(Producto, on_delete = models.CASCADE)
	cantidad		= models.IntegerField()

class Venta(models.Model):
	cliente 		= models.ForeignKey(Cliente, on_delete = models.CASCADE)
	detalleVenta 	= models.ForeignKey(DetalleVenta, on_delete = models.CASCADE)	
	fecha			= models.DateTimeField(auto_now_add=True)	