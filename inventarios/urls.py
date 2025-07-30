from django.urls import path, re_path
from .views import movimientos


urlpatterns = [
    path('movimientos',movimientos, name='movimientos'),
]