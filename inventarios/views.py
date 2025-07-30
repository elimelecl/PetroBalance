from django.shortcuts import render

def movimientos(request):
    return render(request, "inventarios/main.html")
