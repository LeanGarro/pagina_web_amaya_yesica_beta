from django import forms
from . import models

class form_Pais(forms.Form):
    class Meta:
        model = models.Pais
        verbose_name = "Pais"
        verbose_name_plural = "Paises"
        model = models.Pais
        fields = '__all__'

    
class form_del_proveedor(forms.ModelForm):
    class Meta:
        verbose_name = "proveedor"
        verbose_name_plural = "proveedores"
        model = models.proveedor
        fields = ["name", "surname", "email", "phone", "country", "provee"]