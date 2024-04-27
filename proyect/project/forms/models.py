from django.db import models

from django.core.validators import RegexValidator
    
class proveedor(models.Model):
    imagen = models.ImageField(upload_to="proveedor/", null=True, blank=True, verbose_name="Imagen", help_text="Imagen del Proveedor" )
    name = models.CharField(max_length=60, null=False, blank=False, unique=False,verbose_name="Nombre", help_text="Nombre del Proveedor")
    num_cuenta = models.IntegerField(null=True, blank=False,unique=True, verbose_name="Numero de cuenta", help_text="Número de cuenta del Proveedor")
    cuit = models.IntegerField(null=True, blank=False,unique=True, verbose_name="Cuit", help_text="Cuit del Proveedor")
    email = models.EmailField(max_length=254, null=False, blank=False, unique=True, verbose_name="E-mail", help_text="E-mail del Proveedor")
    direccion = models.CharField(max_length=150, null=True, blank=False, verbose_name="direccion", help_text="Domicilio del Proveedor")
    whatsapp = models.IntegerField(null=True, blank=False,unique=True, verbose_name="Whatsapp", help_text="Whatsapp del Proveedor")
    phone = models.CharField(max_length=15,null=False, blank=False, unique=True, verbose_name="Teléfono", help_text="Teléfono del Proveedor", validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="El número de teléfono debe tener un formato válido.")])
    provee = models.TextField(max_length=150, null=False, blank=False, verbose_name="provee", help_text="que provee")
    def __str__(self):
        return f"ID: {self.pk} | {self.name} Cuit: {self.cuit}"

    