from django.shortcuts import render, redirect
from .forms import CreartareaForm, CreargrupotareaForm
from .models import Creartarea
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

# saque estas funciones Curso Django de Developerpepiur


