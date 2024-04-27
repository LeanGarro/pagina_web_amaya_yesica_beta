from django import forms
from . import models

class form_de_producto(forms.ModelForm):
    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        model = models.productos
        fields = '__all__'

class form_de_marca(forms.ModelForm):
    class Meta:
        verbose_name = "marca"
        verbose_name_plural = "marcas"
        model = models.marcas
        fields = '__all__'

class form_de_unidad(forms.ModelForm):
    class Meta:
        verbose_name = "unidad"
        verbose_name_plural = "unidades"
        model = models.unidades
        fields = '__all__'