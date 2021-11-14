from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class Usuario_Manager(BaseUserManager):
    def create_user(self, nombre_usuario, correo, nombres, password = None):
        usuario = self.model(
            nombre_usuario=nombre_usuario,
            correo = self.normalize_email(correo),
            nombres=nombres,
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self,nombre_usuario,correo,nombres,password):
        usuario = self.create_user(
            nombre_usuario=nombre_usuario,
            correo = self.normalize_email(correo),
            nombres=nombres,
            
        )
        
        usuario.usuario_administrador = True
        usuario.save()
        return usuario



class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    nombre_usuario= models.CharField("Nombre de Usuario",unique = True, max_length=30)
    correo= models.EmailField("Correo electronico ",unique = True, max_length=30)
    nombres= models.CharField("Nombres", max_length=30, blank= False, null=True)
    apellidos= models.CharField("Apellidos", max_length=30, blank= False, null=True)
    usuario_avtivo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    objects= Usuario_Manager()
    fecha_creacion= models.DateField(auto_now=True, auto_now_add=False)
    


    USERNAME_FIELD = 'nombre_usuario'
    REQUIRED_FIELDS = ['correo', 'nombres']


    def __str__(self):
        return f'Usuario {self.nombre_usuario}, {self.apellidos}'

    def has_perm(self,perm,obj= None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property 
    def is_staff(self):
        return self.usuario_administrador 

# Create your models here.
