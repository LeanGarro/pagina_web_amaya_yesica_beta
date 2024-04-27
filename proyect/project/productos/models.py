from django.db import models
from forms.models import proveedor

class marcas(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, unique=True, verbose_name="Nombre", help_text="Nombre de la Marca")
    
    def __str__(self):
        return self.name

class unidades(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, unique=True, verbose_name="Nombre", help_text="Nombre de la Unidad")
    
    def __str__(self):
        return self.name

class productos(models.Model):
    imagen = models.ImageField(upload_to="producto/", null=True, blank=True, verbose_name="Imagen", help_text="Imagen del Producto")
    name = models.CharField(max_length=150, null=False, blank=False, unique=True, verbose_name="Nombre", help_text="Nombre del producto")
    marca = models.ForeignKey(marcas, on_delete=models.DO_NOTHING, null=True, blank=False)
    proveedor = models.ForeignKey(proveedor, on_delete=models.DO_NOTHING, null=True, blank=True)
    descripcion = models.TextField(max_length=200, null=False, blank=False, verbose_name="Descripción", help_text="Descripción del Producto")
    unidad = models.ForeignKey(unidades, on_delete=models.DO_NOTHING, null=True, blank=False)
    link = models.URLField(max_length=500, null=True, blank=True, verbose_name="Link", help_text="Link del Producto en Mercado Libre")
    
    def __str__(self):
        return f"ID: {self.pk} | {self.name} Marca: {self.marca} Unidad: {self.unidad}"