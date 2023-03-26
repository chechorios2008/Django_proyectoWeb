from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.

def servicios(request):

    #Importo todos los objetos de la clase servicio
    servicios=Servicio.objects.all() 
    return render(request, "servicios/servicios.html", {"servicios": servicios}) #Para que los muestre