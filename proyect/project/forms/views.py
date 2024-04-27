from django.shortcuts import render

from django.http import HttpResponse
from . import models
from . import forms

from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
    

def busqueda_proveedor(request):
    """ muestra la vista de busqueda de proveedor """
    return render(request, "./template/proveedor/busqueda_proveedor.html")

def buscar(request):
    """ busca un proveedor en la DB y lo muestra"""
    if request.GET['buscar_proveedor']:
        name = request.GET['buscar_proveedor']
        proveedor = models.proveedor.objects.filter(
            Q(name__icontains=name) |
            Q(email__icontains = name) |
            Q(provee__icontains = name)).distinct()
        
        return render(request, "./template/proveedor/busqueda_proveedor.html", {"resultado_proveedor": proveedor})
        
    else:
        respuesta = "No enviaste datos"
    
    return render(request, "./template/proveedor/busqueda_proveedor.html", {"respuesta_busqueda": respuesta})


class proveedorList(ListView):
    """ lista los proveedores en la DB """
    model = models.proveedor
    template_name = "proveedor/leer_proveedores.html"
    context_object_name = "proveedor"
    
class proveedordetalle(DetailView):
    """ muestra el detalle de un proveedor en una nueva pagina"""
    model = models.proveedor
    template_name = "proveedor/proveedor_detail.html"
    context_object_name = "proveedor"
    
class proveedorCreate(CreateView):
    """ crea un nuevo proveedor """
    model = models.proveedor
    template_name = "proveedor/form_proveedor.html"
    fields = ["name", "surname", "email", "phone", "country", "provee"]
    success_url = reverse_lazy("proveedor_list")
    
class proveedorUpdate(UpdateView):
    """ acrualiza un proveedor de la BD """
    model = models.proveedor
    from_class = forms.form_del_proveedor
    template_name = "proveedor/form_proveedor.html"
    fields = ["name", "surname", "email", "phone", "country", "provee"]
    success_url = reverse_lazy("proveedor_list")
    
class proveedorDelete(DeleteView):
    """ elimina un proveedor de la BD """
    model = models.proveedor
    template_name = "proveedor/proveedor_delete.html"
    success_url = reverse_lazy("proveedor_list")
    

    
