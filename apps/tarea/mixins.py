from django.shortcuts import redirect

class LoginySuperUsuarioMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.usuario_diseñador:
                return super().dispatch(request, *args, **kwargs)
        return redirect('index')