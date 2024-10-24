from django.shortcuts import render
from .models import Aviones 

# Create your views here.
def listandoAviones(request):
    losaviones=Aviones.objects.all()
    return render(request,"GestionarAviones.html",{"misaviones":losaviones})