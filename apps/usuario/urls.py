from re import template
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from .views import editarUsuario,crear_Usuario, eliminarUsuario, listarUsuario, InicioUsuarios, reportePdf, tablero
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('InicioUsuarios/', (InicioUsuarios.as_view()), name='InicioUsuarios'),
    path('crear_usuario/', (crear_Usuario.as_view()), name='crear_usuario'),
    path('listarUsuario/', (listarUsuario.as_view()), name='listarUsuario'),
    path('editarUsuario/<id>/', login_required(editarUsuario), name= 'editarUsuario'),
    path('eliminarUsuario/<int:pk>', (eliminarUsuario.as_view()), name='eliminarUsuario'),
    path('reportePdf/', (reportePdf.as_view()), name='reportePdf'),
    path('tablero/', (tablero.as_view()),name='tablero' ),
]