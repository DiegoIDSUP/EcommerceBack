from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app.viewsets import UserViewSet, DomicilioViewSet, ComentarioViewSet,SessionslogViewSet, ProductoViewSet,VendedoresViewSet,PedidoViewSet,ReporteViewSet,  UserViewSet2, DomicilioViewSet2, UserViewSet2, VendedoresViewSet2,  SessionslogViewSet2,PedidoViewSet2, ComentarioViewSet2, SessionslogViewSet3,ComentarioViewSet3,ReporteViewSet2
from app.views import ChargeView
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('usuarios',UserViewSet)
router.register('domicilios',DomicilioViewSet)
router.register('sessionslogs',SessionslogViewSet)
router.register('productos',ProductoViewSet)
router.register('vendedores',VendedoresViewSet)
router.register('pedidos',PedidoViewSet)
router.register('comentarios',ComentarioViewSet)
router.register('reportes',ReporteViewSet)

router.register('usuarios2',UserViewSet2)
router.register('domicilios2',DomicilioViewSet2)
router.register('sessionslogs2',SessionslogViewSet2)
router.register('vendedores2',VendedoresViewSet2)
router.register('pedidos2',PedidoViewSet2)
router.register('comentarios2',ComentarioViewSet2)
router.register('reportes2',ReporteViewSet2)

router.register('sessionslogs3',SessionslogViewSet3)
router.register('comentarios3',ComentarioViewSet3)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include(router.urls)),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('app/auth/', include('rest_auth.urls')),
    path('app/registration/', include('rest_auth.registration.urls')),
    path('app/charges/', ChargeView.as_view() ),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)