# backend/siscosed/api/views.py
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from .models import Usuario
from .models import Informe

def user_is_admin(user):
    return user.rol == 'admin' or user.rol == 'superadmin'

def user_is_superadmin(user):
    return user.rol == 'superadmin'

@login_required
@user_passes_test(user_is_admin)
def some_admin_view(request):
    # Lógica para vista de administrador
    return render(request, 'admin_view.html')

@login_required
@user_passes_test(user_is_superadmin)
def some_superadmin_view(request):
    # Lógica para vista de superadministrador
    return render(request, 'superadmin_view.html')


def ver_auditoria_informe(request, informe_id):
    informe = Informe.objects.get(idinforme=informe_id)
    return render(request, 'auditoria_informe.html', {
        'informe': informe
    })