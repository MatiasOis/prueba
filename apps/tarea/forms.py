from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.db import models
from django.db.models import fields
from django.forms.widgets import Select
from .models import CrearGrupotarea, Creartarea

class CreartareaForm(forms.ModelForm):
    class Meta:
        model = Creartarea
        fields = {'nombre_tarea','responsable','fecha_entrega','descripcion','referencia','pendiente'}
        widgets = {
            'nombre_tarea': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre de la tarea'
                }
            ),
            # -------------para seleccionar campo en foreign key
            'responsable': forms.Select(
                attrs = {
                    'class':'form-control'
                }
            ),
            'fecha_entrega': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese descripcion de la tarea'
                }
            ),
            # hacer la wea para que muestre las referencia (en el modelo iwal)
            'referencia': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese la tarea de referencia'
                }
            ),
            

        }

class CreargrupotareaForm(forms.ModelForm):
    class Meta:
        model = CrearGrupotarea
        fields = {'nombre_Grupo_tarea','responsable','fecha_entrega','descripcion','tarea1', 'tarea2', 'tarea3','pendiente'}
        widgets = {
            'nombre_Grupo_tarea': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre del grupo de tareas'
                }
            ),
            # -------------para seleccionar campo en foreign key
            'responsable': forms.Select(
                attrs = {
                    'class':'form-control'
                }
            ),
            'tarea1': forms.Select(
                attrs = {
                    'class':'form-control',
                }
                ),
            'tarea2': forms.Select(
                attrs = {
                    'class':'form-control',
                }
                ),
            'tarea3': forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),
            'fecha_entrega': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese descripcion de la tarea'
                }
            ),
            
            

        }