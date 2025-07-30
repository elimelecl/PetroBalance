from django.shortcuts import render

# Create your views here.
def reportes(request):
    return render(request, "reportes.html")

def resumen_diario(request):
    return render(request, "resumen_diario.html")

def volumen_producto(request):
    return render(request, "volumen_producto.html")

def exportar_datos(request):
    return render(request, "exportar_datos.html")