from django.db import models
from apps.usuario.models import Usuario

class Creartarea(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_tarea = models.CharField(max_length=30, blank= False, null= False)
    # para hacer la FK
    responsable = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    creacion_tarea = models.DateField(auto_now=True, auto_now_add=False)
    fecha_entrega= models.DateField(blank= False, null= False)
    descripcion = models.CharField(max_length=100, blank= False, null= True)
    referencia = models.CharField(max_length=30, blank= False, null= True)
    pendiente = models.BooleanField(null=True)
    
    

    class Meta:
        verbose_name = 'Crear tarea' 
        verbose_name_plural = 'Crear tareas' 

    def __str__(self):
        return self.nombre_tarea

class CrearGrupotarea(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_Grupo_tarea = models.CharField(max_length=30, blank= False, null= False)
    # para hacer la FK
    responsable = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_entrega= models.DateField(blank= False, null= False)
    descripcion = models.CharField(max_length=100, blank= False, null= True)
    pendiente = models.BooleanField(null=True)
    tarea1 = models.ForeignKey(Creartarea, related_name='tarea1',on_delete=models.CASCADE)
    tarea2 = models.ForeignKey(Creartarea,related_name='tarea2' ,on_delete=models.CASCADE)
    tarea3 = models.ForeignKey(Creartarea,related_name='tarea3' ,on_delete=models.CASCADE)
    
    

    class Meta:
        verbose_name = 'Crear grupo tarea' 
        verbose_name_plural = 'Crear grupo tareas' 

    def __str__(self):
        return self.nombre_Grupo_tarea


class rechazarTarea(models.Model):
    id = models.AutoField(primary_key=True)
    Tarea = models.ForeignKey(Creartarea, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=100, blank= False, null= True)

# Create your models here.
