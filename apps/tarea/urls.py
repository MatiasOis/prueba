from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import crear_Tarea, listarTarea, editarTarea, diseñador, rechazar, listarTareaAdmin, listarFlujoTarea, listarTareaPdf


urlpatterns = [
    path('crear_tarea/', login_required(crear_Tarea), name='crear_tarea'),
    path('listarTarea/', login_required(listarTarea), name= 'listarTarea'),
    path('editarTarea/<id>', login_required(editarTarea), name= 'editarTarea'),
    path('grupo_de_tareas/', login_required(diseñador), name= 'grupo_de_tareas'),
    path('rechazar/<id>', login_required(rechazar), name= 'rechazar'),
    path('listarTareadmin/', login_required(listarTareaAdmin), name= 'listarTareaAdmin'),
    path('listarFlujoTarea/', login_required(listarFlujoTarea), name= 'listarFlujoTarea'),
    path('listarTareaPdf/', login_required(listarTareaPdf.as_view()), name='listarTareaPdf'),
]