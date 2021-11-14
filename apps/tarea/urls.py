from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import crear_Tarea, listarTarea, editarTarea, diseñador


urlpatterns = [
    path('crear_tarea/', login_required(crear_Tarea), name='crear_tarea'),
    path('listarTarea/', login_required(listarTarea), name= 'listarTarea'),
    path('editarTarea/<id>', login_required(editarTarea), name= 'editarTarea'),
    path('grupo_de_tareas/', login_required(diseñador), name= 'grupo_de_tareas'),
]