from django.db import models
from clientes.models import Cliente
# Create your models here.

class Operacion(models.Model):
    """Aquí, se Contempla todas las posibles operaciones que se pueda realizar a tosdos los medios.
    Ejemplos de Operaciones: Cargue, Descargue, Transferencia"""
    nombre = models.CharField(max_length=30)
    consular_saldo_kardex = models.BooleanField(
        default=False,
        help_text = 'Marcar, si al crear una orden de trabajo, se consulta el saldo en tanque'
    )
    requiere_movimiento_de_producto = models.BooleanField(
        default=True,
        help_text = "Sirve para indicar si se agrega 'movimientos' al momento de la creación de la Orden de Trabajo"
    )
    afectacion_volumen = models.BooleanField(default=True) # Este campo indica si la operación implica una variación en
                                                           # el volumen de los tanques asiciados.
                                                           # Ejemplo de operaciones que no implican variación: Heating.
    tipo = models.TextField(
        max_length=30,
        choices=(
            ('Salida', 'Salida'),
            ('Entrada', 'Entrada'),
            ('Entamborado', 'Entamborado'),
            ('Recirculacion', 'Recirculacion'),
            ('Transferencia', 'Transferencia'),
            ('Salida Tambores Llenos', 'Salida Tambores Llenos'),
            ('Entrada Tambores Llenos', 'Entrada Tambores Llenos'),
            ('Salida Tambores Vacios', 'Salida Tambores Vacios'),
            ('Entrada Tambores Vacios', 'Entrada Tambores Vacios'),
        ),
        default='Salida',
    )
    def __str__(self):
        return self.nombre

class Tanque(models.Model):
    nombre = models.CharField(max_length=100)
    limite_superior_zona_critica = models.IntegerField(null=True, blank = True)
    limite_inferior_zona_critica = models.IntegerField(null=True, blank = True)
    tipo = models.CharField(max_length = 100, choices = (
        ('Techo Fijo', 'Techo Fijo'),
        ('Techo Flotante', 'Techo Flotante'),
        ('Bodega', 'Bodega')
    ))


class TipoMedio(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='static/imagenes/tipos_medio', blank=True, null = True)
    tipo = models.CharField(max_length=100, choices = (
        ('Entamborado', 'Entamborado'),
        ('Carro Tanque', 'Carro Tanque'),
        ('Buque', 'Buque'),
        ('Barcaza', 'Barcaza'),
        ('Transferencia', 'Transferencia'),
        ('Calentamiento', 'Calentamiento'),
        ('Pigging', 'Pigging'),
    )
                            )
    operaciones_realizables = models.ManyToManyField(Operacion, related_name = 'operaciones_realizables',
                                                     help_text='El tipo de medio solo admite las operaciones seleccionadas')
    consulta_saldo_operacion = models.ManyToManyField(Operacion, related_name = 'consulta_saldo_operacion',
                                                      help_text='Se consultará saldo en el tanque cuando se realice un movimiento que contenga esta operacion')

class Unidad(models.Model):
    nombre  = models.CharField(max_length= 100)
    tipo = models.ForeignKey(TipoMedio, on_delete=models.CASCADE, null=True, blank = True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank = True)
    def __str__(self):
        return self.nombre

