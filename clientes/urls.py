from django.urls import path, re_path
from .views import clientes


urlpatterns = [
    path('', clientes, name='clientes'),
    ]