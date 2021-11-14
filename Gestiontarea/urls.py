"""Gestiontarea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import conf, path, include
# from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from apps.tarea.views import home
from django.conf.urls import url
from apps.usuario.views import Login, logoutUsuario
# from apps.usuario.views import listarUsuario

urlpatterns = [
    path('home/', login_required(home), name='index'),
    path('admin/', admin.site.urls),
    path('tarea/', include(('apps.tarea.urls', 'tarea'))),
    path('usuario/', include(('apps.usuario.urls', 'usuario'))),
    # path('usuario/view',listarUsuario, name='ListaUsuario'),
    path('accounts/login/',Login.as_view(), name='login'),
    path('logout/',login_required(logoutUsuario), name='logout'),
    path('diseñador/', include(('apps.tarea.urls', 'diseñador'))),
    url('', include('pwa.urls'))
    



    # url(r'^$', LoginView.as_view(template_name='login.html'), name='login'),
   
]
