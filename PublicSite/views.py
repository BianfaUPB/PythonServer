from django.shortcuts import render, HttpResponse
from PublicSite.models import Usuario

# Create your views here.
def usuarios(request):
    usuarios = Usuario.objects.all()
    
    return HttpResponse(usuarios.values_list())
    
def usuario(request, usuario):
    usuario = Usuario.objects.get(usuario=usuario)

    return render(request, "usuario.html", {
        "usuario": usuario
    })

def crear_usuario(request, nombre, email, usuario):
    nuevoUsuario = Usuario(
        3,
        nombre,
        email,
        usuario
    )

    nuevoUsuario.save()

    return HttpResponse("Usuario guardado exitosamente")

def actualizar_usuario(request, id, nombre, email, usuario):
    usuarioActual = Usuario.objects.get(id=id)

    usuarioActual.nombre = nombre
    usuarioActual.email = email
    usuarioActual.usuario = usuario

    usuarioActual.save()

    return HttpResponse("Usuario actualizadó exitosamente")

def index(request):
    years = list(range(2020, 2051))

    return render(request,"index.html",{
        'years': years
    })

def hola_mundo(request):
    return render(request,"hola_mundo.html")

def sobre_nosotros(request):
    return render(request,"sobre_nosotros.html")