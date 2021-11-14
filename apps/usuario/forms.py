from django import forms
from django.contrib.auth.forms import AuthenticationForm
from apps.usuario.models import Usuario
from django.db.models import fields
from .models import Usuario



class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


class UsuarioForm(forms.ModelForm):


    contra1 = forms.CharField(label = 'Contraseña',widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese la contraseña',
            'id': 'contra1',
            'required':'required',
        }
    ))

    contra2 = forms.CharField(label = 'Contraseña de Confirmación', widget = forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Confirme la contraseña',
            'id': 'contra2',
            'required': 'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = {'nombre_usuario','correo','nombres','apellidos'}
        widgets = {
            'nombre_usuario': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre de usuario'
                }
            ),
            'correo': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese el correo del usuario'
                }
            ),
            'nombres': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el/los nombre del usuario'
                }
            ),
            'apellidos': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el/los apellido del usuario'
                }
            )
            
            
            }
    def clean_contra2(self):
        #Validación de Contraseña

        contra1 = self.cleaned_data.get('contra1')
        contra2 = self.cleaned_data.get('contra2')
        if contra1 != contra2:
            raise forms.ValidationError('Las contraseñas no son iguales, intene nuevamente uwu')
        return contra2

    def save(self,commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['contra1'])
        if commit:
            user.save()
        return user

