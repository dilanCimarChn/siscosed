from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        # Autenticación
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'role': user.rol})
        else:
            return JsonResponse({'success': False, 'error': 'Credenciales inválidas'}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@login_required
def redirect_based_on_role(request):
    return JsonResponse({'role': request.user.rol})

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def normal_dashboard(request):
    if request.user.rol != 'normal':
        return JsonResponse({'error': 'Acceso no autorizado'}, status=403)
    return JsonResponse({'message': 'Bienvenido al panel de usuario normal.'})

@login_required
def admin_dashboard(request):
    if request.user.rol != 'admin':
        return JsonResponse({'error': 'Acceso no autorizado'}, status=403)
    return JsonResponse({'message': 'Bienvenido al panel de administrador.'})

@login_required
def superadmin_dashboard(request):
    if request.user.rol != 'superadmin':
        return JsonResponse({'error': 'Acceso no autorizado'}, status=403)
    return JsonResponse({'message': 'Bienvenido al panel de superadministrador.'})
