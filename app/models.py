from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    stock = models.IntegerField()
    precio = models.FloatField()
    show = models.BooleanField(blank=True)
    imagen = models.ImageField(upload_to="Productos")
    class Meta:
        db_table='productos'

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True)
    domicilio = models.ForeignKey('Domicilio', on_delete=models.SET_NULL, null=True)
    stock = models.IntegerField()
    release_date = models.DateTimeField()
    class Meta:
        db_table='pedidos'
        
class Vendedores(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    verified = models.BooleanField(blank=True)
    nombre = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    rfc = models.CharField(max_length=200,blank=True)
    class Meta:
        db_table='vendedores'
        
class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True)
    comentario = models.CharField(max_length=200)
    class Meta:
        db_table='comentarios'
        
class Reporte(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True)
    comentario = models.CharField(max_length=200)
    class Meta:
        db_table='reportes'

class Domicilio(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    calle = models.CharField(max_length=200)
    num = models.CharField(max_length=200)
    numInt = models.CharField(max_length=200,blank=True)
    referencia = models.CharField(max_length=200,blank=True)
    colonia = models.CharField(max_length=200)
    cp = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    class Meta:
        db_table='domicilios'

class Sessionslog(models.Model):
    email = models.CharField(max_length=200)
    action = models.CharField(max_length=200)
    intentos = models.IntegerField()
    release_date = models.DateTimeField()
    class Meta:
        db_table='sessionslog'