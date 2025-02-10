from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt
from .views import UsuarioViewSet, login_view, redirect_based_on_role, gestion_usuarios, get_csrf_token

# Crea el enrutador para las vistas de la API
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('login/', login_view, name='login'),  # Ruta para login
    path('redirect/', redirect_based_on_role, name='redirect_based_on_role'),  # Redirección según el rol
    path('gestion_usuarios/', gestion_usuarios, name='gestion_usuarios'),  # Ruta para la gestión de usuarios
    path('get_csrf_token/', csrf_exempt(get_csrf_token), name='get_csrf_token'),  # Aquí se ha corregido el error
    path('', include(router.urls)),  # Incluir las URLs del enrutador para la API
]
