from re import template
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from .views import crear_Usuario, eliminarUsuario, listarUsuario, InicioUsuarios

urlpatterns = [
    path('InicioUsuarios/', (InicioUsuarios.as_view()), name='InicioUsuarios'),
    path('crear_usuario/', (crear_Usuario.as_view()), name='crear_usuario'),
    path('listarUsuario/', (listarUsuario.as_view()), name='listarUsuario'),
    path('eliminarUsuario/<int:pk>', (eliminarUsuario.as_view()), name='eliminarUsuario'),
]