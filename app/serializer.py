from rest_framework import serializers
from django.contrib.auth.models import User
from app.models import Domicilio,Sessionslog,Producto,Vendedores,Comentario,Reporte,Pedido

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        
class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'
        
class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'
        
class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'
        
class VendedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedores
        fields = '__all__'
        
class DomicilioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domicilio
        fields = '__all__'
        
class SessionslogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sessionslog
        fields = '__all__'
        
