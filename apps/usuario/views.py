from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404
from django.urls import reverse_lazy
from django.urls.base import is_valid_path
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache 
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from xhtml2pdf import context
from .forms import LoginForm, UsuarioForm
from apps.usuario.models import Usuario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, TemplateView, DeleteView, View
# importacion del mixin
from apps.usuario.mixins import LoginySuperUsuarioMixin
from django.db import models
from .forms import LoginForm, UsuarioForm

# Create your views here.
from .models import Usuario
from django.http import HttpResponse
from apps.usuario.utils import render_to_pdf


class home(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

class tablero(LoginRequiredMixin, TemplateView):
    template_name = 'tablero.html'

class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')
 
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


def crear_Usuario(request): 
    if request.method == 'POST':      
        print(request.POST)
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()
        return render(request, 'usuario/register.html')    
    else:
        usuario_form = UsuarioForm
    return render(request, 'usuario/register.html', {'usuario_form':usuario_form})

def editarUsuario(request,id):
    # ediUsuario = Usuario.objects.get( id = id)
    # if request.method == 'GET':
    #     usuario_form = UsuarioForm(instance = ediUsuario)
    # else:
        usuario = get_object_or_404(Usuario, id= id)

        data ={
            'form': UsuarioForm(instance=usuario)
        }
        if request.method == 'POST':
            formulario = UsuarioForm(data=request.POST, instance=usuario, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
            data['form'] = formulario
        # usuario_form = UsuarioForm(request.POST, instance= ediUsuario)
        # if usuario_form.is_valid():
        #     usuario_form.save()
        # return redirect ('index')
        return render (request,'usuario/editar-usuario.html',data)

# el archivo mixin se hizo para el administrador y fue aplicado en esta vista para que solo el super usuario acceda al template referenciado

class InicioUsuarios(LoginySuperUsuarioMixin,TemplateView):
    template_name='usuario/listarUsuario.html'


# lista de usuarios para admin
class listarUsuario(LoginySuperUsuarioMixin, ListView):
    model = Usuario
    Usuarios= Usuario
    template_name= 'Usuario/view.html'
    context_object_name = 'usuarios'
    
    def get_queryset(self):
        return self.Usuarios.objects.filter(usuario_avtivo= True)
        

class reportePdf(View):
    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        data = {
            'usuarios' : usuarios
        }
        pdf = render_to_pdf('usuario/listarUsuario.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class crear_Usuario(LoginySuperUsuarioMixin, CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/register.html'
    success_url = reverse_lazy('usuario:listarUsuario')



class eliminarUsuario(LoginySuperUsuarioMixin, DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuario:listarUsuario')
