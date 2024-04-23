from django.db import models

from django.core.validators import RegexValidator

class Pais(models.Model):
    name = models.CharField(max_length=57)
    
    def __str__(self):
        return self.name
    
class proveedor(models.Model):
    imagen = models.ImageField(upload_to="proveedor", null=True, blank=True, verbose_name="Imagen", help_text="Imagen del Proveedor" )
    name = models.CharField(max_length=60, null=False, blank=False, unique=False,verbose_name="Nombre", help_text="Nombre del Proveedor")
    surname = models.CharField(max_length=60, null=False, blank=False, unique=False, verbose_name="Apellidos", help_text="Apellidos del Proveedor")
    email = models.EmailField(max_length=254, null=False, blank=False, unique=True, verbose_name="E-mail", help_text="E-mail del Proveedor")
    phone = models.CharField(max_length=15,null=False, blank=False, unique=True, verbose_name="Teléfono", help_text="Teléfono del Proveedor", validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="El número de teléfono debe tener un formato válido.")])
    country = models.ForeignKey(Pais, on_delete=models.CASCADE, verbose_name="País", help_text="País del Proveedor", null=True, blank=True)
    provee = models.TextField(max_length=150, null=False, blank=False, verbose_name="provee", help_text="que provee")
    
    def __str__(self):
        return f"ID: {self.id} | {self.name} {self.surname}"

    