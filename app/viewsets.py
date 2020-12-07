from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from app.models import Domicilio,Sessionslog,Producto,Vendedores,Pedido,Comentario,Reporte
from app.serializer import UserSerializer,DomicilioSerializer,SessionslogSerializer,ProductoSerializer,VendedoresSerializer,PedidoSerializer,ComentarioSerializer,ReporteSerializer
from django_filters.rest_framework import DjangoFilterBackend
import openpay

class UserViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ReporteViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['producto']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

class ReporteViewSet2(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['producto']
    permission_classes = [IsAuthenticated]
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['producto']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class ComentarioViewSet2(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['producto']
    permission_classes = [IsAuthenticated]
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user','show']
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ComentarioViewSet3(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['producto']
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class VendedoresViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user','verified']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vendedores.objects.all()
    serializer_class = VendedoresSerializer

class DomicilioViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Domicilio.objects.all()
    serializer_class = DomicilioSerializer

class SessionslogViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Sessionslog.objects.all()
    serializer_class = SessionslogSerializer
    
class UserViewSet2(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email']
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PedidoViewSet2(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class VendedoresViewSet2(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user','verified']
    permission_classes = [IsAuthenticated]
    queryset = Vendedores.objects.all()
    serializer_class = VendedoresSerializer

class DomicilioViewSet2(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']
    permission_classes = [IsAuthenticated]
    queryset = Domicilio.objects.all()
    serializer_class = DomicilioSerializer

class SessionslogViewSet2(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Sessionslog.objects.all()
    serializer_class = SessionslogSerializer

class SessionslogViewSet3(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email']
    queryset = Sessionslog.objects.all()
    serializer_class = SessionslogSerializer
