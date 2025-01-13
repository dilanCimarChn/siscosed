from django.urls import path
from . import views  # Este es el archivo views.py de tu aplicación "api"

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('redirect/', views.redirect_based_on_role, name='redirect_based_on_role'),
    path('normal_dashboard/', views.normal_dashboard, name='normal_dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('superadmin_dashboard/', views.superadmin_dashboard, name='superadmin_dashboard'),
]
