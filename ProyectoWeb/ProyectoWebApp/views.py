from django.shortcuts import render

from servicios.models import Servicio

from carro.carro import Carro



# Create your views here.

def home(request):

    carro = Carro(request)
    return render(request, "ProyectoWebApp/home.html")