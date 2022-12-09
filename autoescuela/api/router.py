from rest_framework.routers import DefaultRouter
from autoescuela.api.views import ExamenViewSet, PreguntaViewSet, PermisoViewSet, TemaViewSet, UsuarioViewSet, Examen_UsuarioViewSet, UserLoginViewSet

router_autoescuela = DefaultRouter()

router_autoescuela.register(prefix='examen', viewset=ExamenViewSet, basename='examen')
router_autoescuela.register(prefix='pregunta', viewset=PreguntaViewSet, basename='pregunta')
router_autoescuela.register(prefix='permiso', viewset=PermisoViewSet, basename='permiso')
router_autoescuela.register(prefix='tema', viewset=TemaViewSet, basename='tema')
router_autoescuela.register(prefix='usuario', viewset=UsuarioViewSet, basename='usuario')
router_autoescuela.register(prefix='examen_usuario', viewset=Examen_UsuarioViewSet, basename='examen_usuario')
router_autoescuela.register(prefix='usuariologged', viewset=UserLoginViewSet, basename='usuario')
