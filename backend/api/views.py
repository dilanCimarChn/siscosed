from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
import json

from .models import Usuario
from .serializers import UsuarioSerializer

# Vista de login sin autenticación, con CSRF
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        # Autenticación
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.estado == 1:  # Validación del estado del usuario
                login(request, user)
                return JsonResponse({'success': True, 'role': user.rol})
            else:
                return JsonResponse({'success': False, 'error': 'El usuario está deshabilitado'}, status=403)
        else:
            return JsonResponse({'success': False, 'error': 'Credenciales inválidas'}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Redirigir basado en el rol
def redirect_based_on_role(request):
    return JsonResponse({'role': request.user.rol})

# Vista de gestión de usuarios sin restricciones de autenticación
def gestion_usuarios(request):
    usuarios = Usuario.objects.all()
    usuarios_data = list(usuarios.values('id', 'email', 'rol', 'estado', 'telefono', 'celular', 'domicilio'))
    return JsonResponse({'usuarios': usuarios_data}, safe=False)

# API REST para los usuarios
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    # Filtrar usuarios por rol o estado
    @action(detail=False, methods=['get'])
    def filter_users(self, request):
        rol = request.query_params.get('rol', None)
        estado = request.query_params.get('estado', None)

        usuarios = Usuario.objects.all()
        if rol:
            usuarios = usuarios.filter(rol=rol)
        if estado:
            usuarios = usuarios.filter(estado=estado)

        serializer = self.get_serializer(usuarios, many=True)
        return Response(serializer.data)

    # Cambiar el estado de un usuario (habilitar/deshabilitar)
    @action(detail=True, methods=['put'])
    def toggle_status(self, request, pk=None):
        usuario = self.get_object()
        usuario.estado = 0 if usuario.estado == 1 else 1
        usuario.save()
        return Response({'status': 'Usuario actualizado', 'estado': usuario.estado})

    # Cambiar el rol de un usuario
    @action(detail=True, methods=['put'])
    def change_role(self, request, pk=None):
        usuario = self.get_object()
        new_rol = request.data.get('rol')
        if new_rol:
            usuario.rol = new_rol
            usuario.save()
            return Response({'status': 'Rol actualizado', 'rol': usuario.rol})
        return Response({'error': 'Rol no proporcionado'}, status=400)

    # Actualizar los detalles de un usuario (nombre, apellido, etc.)
    @action(detail=True, methods=['put'])
    def update_user(self, request, pk=None):
        usuario = self.get_object()
        nombre = request.data.get('nombres')
        apellido_paterno = request.data.get('apellidoPaterno')
        apellido_materno = request.data.get('apellidoMaterno')
        telefono = request.data.get('telefono')
        celular = request.data.get('celular')
        domicilio = request.data.get('domicilio')
        foto_perfil = request.data.get('fotoPerfil')

        # Actualizamos los campos proporcionados
        if nombre:
            usuario.nombres = nombre
        if apellido_paterno:
            usuario.apellidoPaterno = apellido_paterno
        if apellido_materno:
            usuario.apellidoMaterno = apellido_materno
        if telefono:
            usuario.telefono = telefono
        if celular:
            usuario.celular = celular
        if domicilio:
            usuario.domicilio = domicilio
        if foto_perfil:
            usuario.fotoPerfil = foto_perfil

        usuario.save()

        return Response({'status': 'Usuario actualizado', 'usuario': usuario.email})

    # Eliminar un usuario
    @action(detail=True, methods=['delete'])
    def delete_user(self, request, pk=None):
        usuario = self.get_object()
        usuario.delete()
        return Response({'status': 'Usuario eliminado'})

    # Cambiar la contraseña de un usuario
    @action(detail=True, methods=['put'])
    def change_password(self, request, pk=None):
        usuario = self.get_object()
        new_password = request.data.get('password')
        if new_password:
            usuario.set_password(new_password)
            usuario.save()
            return Response({'status': 'Contraseña actualizada'})
        return Response({'error': 'No se proporcionó una nueva contraseña'}, status=400)

# Vista para obtener el token CSRF
@csrf_exempt
def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})
