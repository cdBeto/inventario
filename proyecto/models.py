from django.db import models

# Create your models here.
class Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    cantidad = models.CharField(max_length=10, verbose_name='Cantidad')
    descripcion = models.TextField(verbose_name='Descripcion', null=True )

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + "Cantidad: " + self.cantidad + " - " + "Descripcion: " + self.descripcion
        return fila