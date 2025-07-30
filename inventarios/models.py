import datetime
from django.db import models
# Create your models here.
from infrastructura.models import Tanque

UNIDADES_MEDICION = [
   ( 'Barril','Bbls'), ('Kilogramo','Kg'), ('Metro Cubico','M3'), ('Pie Cubico','Ft3'), ('Galon','Gl')
]

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    unidad_medicion = models.CharField(max_length=50, blank=True, null=True, choices = UNIDADES_MEDICION)
    tipo = models.CharField(max_length=100, blank=True, null=True, choices =(
        ('Crudo', 'Crudo'), ('Refinado', 'Refinado'), ('Alcohol', 'Alcohol'), ('Quimico', 'Quimico')))
    def __str__(self):
        return self.nombre
class NombreMovimiento(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format(self.nombre)

class Movimiento(models.Model):
    nombre = models.ForeignKey(NombreMovimiento, on_delete=models.CASCADE, null=True)
    tanque = models.ForeignKey(Tanque, verbose_name='tanque', related_name='tanque_uno', on_delete=models.CASCADE,
                               blank=True, null=True)
    volumen = models.FloatField()
    producto = models.ForeignKey(Producto, blank=True, on_delete=models.PROTECT)
    def __str__(self):
        return '{} / {} / {}'.format(self.id, self.volumen, self.nombre)

    def str_id(self):
        return str(self.id)

    def serializar(self):
        return {
            'id': self.id,
            'nombre': self.nombre.nombre,
            'tanque': self.tanque.nombre,
            'volumen': self.volumen,
            'producto': self.producto.nombre,
        }

class Lote(models.Model):
    """Referencia el lote de un producto. Este se debe actualizar cada vez que se recibe un producto por Buque. En el caso de Mamonal.
       En el caso de Puerto Bahía, hace referencia a lo que se conoce como 'TL'."""
    fecha = models.DateField(null = True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tanque = models.ForeignKey(Tanque, on_delete=models.CASCADE, null = True)
    identificador = models.CharField(max_length=100)
    def __str__(self):
        return 'producto: {} / fecha: {}'.format(self.producto, self.fecha)

    def save(self, *args, **kwargs):
        if not self.id:
            self.fecha = datetime.datetime.now().date()
        return super(Lote, self).save(*args, **kwargs)
    def serializar(self):
        try:
           fecha = self.fecha.strftime("%d/%m/%Y")
        except:
            fecha = ''
        return {
            'id':self.id,
            'fecha':fecha,
            'identificador':self.identificador,
        }



class NombresDeTablas(models.Model):
    nombre = models.CharField(max_length = 50, null = True)
    tanque = models.ForeignKey(Tanque, null = True, blank = True, on_delete = models.CASCADE, related_name = 'Tanque_nombresTabla')
    api = models.IntegerField(null=True, blank=True)
    ajuste_fra = models.FloatField(null = True, blank = True)
    incremento_fra = models.FloatField(null = True, blank = True)
    activa = models.CharField(max_length = 20, choices = (('Si', 'Si'), ('No', 'No')), default = 'Si')
    def __str__(self):
        return '{} / {} / Tanque: {}'.format(self.id, self.nombre, self.tanque)
    class Meta:
        verbose_name_plural = 'Nombres De Tablas'

class TanblaDeAforo(models.Model):
    unidad = models.CharField(max_length = 30, blank = True, choices = (('Cm', 'Cm'),('Mm', 'Mm')))
    cantidad = models.IntegerField(null = True, blank = True)
    barriles = models.FloatField(null = True, blank = True)
    tabla = models.ForeignKey(NombresDeTablas, null = True, blank = True, on_delete = models.CASCADE)
    def __str__(self):
        return 'id: {} /cantidad {} /barriles: {} tabla: {}'.format(self.id,self.cantidad, self.barriles, self.tabla)
    class Meta:
        verbose_name_plural = 'Tablas De Afoto'

class Medicion(models.Model):
    fecha_agregada = models.DateTimeField(auto_now_add=True)
    fecha = models.DateTimeField()
    tanque = models.ForeignKey(Tanque, on_delete=models.CASCADE, related_name='tanque_medicion')
    nivel = models.PositiveIntegerField()
    temperatura = models.FloatField()
    temperatura_ambiente = models.FloatField()
    tabla_liquidacion = models.ForeignKey(NombresDeTablas, null=True, blank=True, on_delete=models.CASCADE)
    api60 = models.FloatField(null=True, blank=True)
    sw = models.FloatField(null=True, blank=True)
    densidad = models.FloatField(null=True, blank=True)
    def __str__(self):
        return f'{self.fecha.__str__()} / {self.tanque.__str__()}'