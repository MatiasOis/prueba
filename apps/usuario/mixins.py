from django.shortcuts import redirect

class LoginySuperUsuarioMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated: 
            # se indica en el request que el usuario debe estar señalado como staff (en nuestro caso el administrador) y con el mixin crear las vistas para este.
            if request.user.is_staff:
                return super().dispatch(request, *args, **kwargs)
        return redirect('index')