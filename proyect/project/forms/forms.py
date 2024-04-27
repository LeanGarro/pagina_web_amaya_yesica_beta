from django import forms
from . import models

    
class form_del_proveedor(forms.ModelForm):
    class Meta:
        verbose_name = "proveedor"
        verbose_name_plural = "proveedores"
        model = models.proveedor
        fields = '__all__'