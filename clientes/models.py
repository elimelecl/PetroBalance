from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    nit = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=30, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    estado_activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre