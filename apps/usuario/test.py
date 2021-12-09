from django.test import TestCase

from apps.usuario.models import Usuario

class UsuarioTestCase(TestCase):

    def setUp(self):
        self.user = Usuario.objects.create_user(
                    nombre_usuario= 'Juancho',
                    correo= 'antunez@gmail.com',
                    nombres='Juanc',
                    apellidos='Antunez',
                    usuario_administrador=False
    )
    def test_user_creation(self):
        assert self.user.usuario_avtivo
        assert self.user.usuario_administrador
        assert self.user.usuario_diseñador