from django.conf import settings
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from .forms import CreartareaForm, CreargrupotareaForm
from .models import Creartarea, CrearGrupotarea
from django.views.generic import View
from apps.tarea.models import Creartarea
from django.http import HttpResponse
from apps.tarea.mixins import LoginySuperUsuarioMixin
from apps.usuario.utils import render_to_pdf
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
# Create your views here.

def home(request):
    return render(request,'index.html')
    
def crear_Tarea( request):
    if request.method == 'POST': 
        print(request.POST)
        tarea_form = CreartareaForm(request.POST)
        if tarea_form.is_valid():
            tarea_form.save()    
        return redirect('index')    
    else:
        tarea_form = CreartareaForm()
    return render(request, 'tarea/creartareas.html', {'tarea_form': tarea_form})

def listarTarea(request):
    Creartareas= Creartarea.objects.all()
    return render(request,'tarea/tables1.html',{'Creartareas': Creartareas} )

def listarTareaAdmin(request):
    Creartareas= Creartarea.objects.all()
    return render(request,'tarea/listarTareaAdmin.html',{'Creartareas': Creartareas} )

def listarFlujoTarea(request):
    CrearGrupotareas= CrearGrupotarea.objects.all()
    return render(request,'tarea/listarFlujos.html',{'CrearGrupotareas': CrearGrupotareas} )

def editarTarea(request,id):
    ediTarea = Creartarea.objects.get( id = id)
    if request.method == 'GET':
        tarea_form = CreartareaForm(instance= ediTarea)
    else:
        tarea_form = CreartareaForm(request.POST, instance= ediTarea)
        if tarea_form.is_valid():
            tarea_form.save()
        return redirect ('index')
    return render (request,'tarea/creartareas.html',{'tarea_form':tarea_form})

def diseñador(request):
    if request.method == 'POST': 
        print(request.POST)
        grupotarea_form = CreargrupotareaForm(request.POST)
        if grupotarea_form.is_valid():
            grupotarea_form.save()    
        return redirect('index')    
    else:
        grupotarea_form = CreargrupotareaForm()
    return render(request, 'tarea/creargrupotareas.html', {'grupotarea_form': grupotarea_form})

def send_email(mail):
    context= {'mail': mail}

    template = get_template('tarea/correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Solicitud de rechazo ',
        'algo mas',
        settings.EMAIL_HOST_USER,
        [mail]
    )
    email.attach_alternative(content, 'text/html')

    email.send()

def rechazar(request,id):
    rechaza = Creartarea.objects.get( id = id)
    if request.method == 'POST':
        mail = request.POST.get('mail')

        send_email(mail)
    
    return render(request, 'tarea/rechazar.html', {})

class listarTareaPdf(View):
    def get(self, request, *args, **kwargs):
        tareas = Creartarea.objects.all()
        data = {
            'tareas' : tareas
        }
        pdf = render_to_pdf('tarea/listarTareaPdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
# saque estas funciones Curso Django de Developerpepiur


