"""
URL configuration for PythonServer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
import PublicSite.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PublicSite.views.index),
    path('hola-mundo/', PublicSite.views.hola_mundo),
    path('sobre-nosotros/', PublicSite.views.sobre_nosotros),
    path('usuarios/', PublicSite.views.usuarios),
    path('usuario/<str:usuario>/', PublicSite.views.usuario),
    path('crear-usuario/<str:nombre>/<str:email>/<str:usuario>/', PublicSite.views.crear_usuario),
    path('actualizar-usuario/<int:id>/<str:nombre>/<str:email>/<str:usuario>/', PublicSite.views.actualizar_usuario),
]
