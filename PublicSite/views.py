from django.shortcuts import render

# Create your views here.
def index(request):
    years = list(range(2020, 2051))

    return render(request,"index.html",{
        'years': years
    })

def hola_mundo(request):
    return render(request,"hola_mundo.html")

def sobre_nosotros(request):
    return render(request,"sobre_nosotros.html")
