from django.shortcuts import render

# Create your views here.

def tanques(request):
    return render(request, "tanques.html")

def productos(request):
    return render(request, "productos.html")

def transporte(request):
    return render(request, "transporte.html")
