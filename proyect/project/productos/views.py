from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models  import Q
from . import models
from . import forms


class productoList(ListView):
    """ lista los clientes en la DB """
    model = models.productos
    template_name = "productos/productos.html"
    context_object_name = "producto"

class productodetalle(DetailView):
    """ muestra el detalle de un producto en una nueva pagina"""
    model = models.productos
    template_name = "productos/producto_detail.html"
    context_object_name = "producto"
        
class productoCreate(CreateView):
    """ crea un nuevo producto """
    model = models.productos
    template_name = "productos/producto_form.html"
    fields = '__all__'
    success_url = reverse_lazy("producto_list")
    
    def form_valid(self, form):
        return super().form_valid(form)

class productoUpdate(UpdateView):
    """ actualiza un producto """
    model = models.productos
    template_name = "productos/producto_form.html"
    fields = '__all__'
    success_url = reverse_lazy("producto_list")
    
    def form_valid(self, form):
        return super().form_valid(form)
    
class productoDelete(DeleteView):
    """ elimina un producto """
    model = models.productos
    template_name = "productos/producto_delete.html"
    success_url = reverse_lazy("producto_list")
    
    def form_valid(self, form):
        return super().form_valid(form)
def busqueda_productos(request):
    """ muestra la vista de busqueda de producto """
    return render(request, "./template/productos/productos_busqueda.html")

def buscar(request):
    """ busca un producto en la DB y lo muestra"""
    respuesta = " "
    
    if request.GET['busqueda_productos']:
        name = request.GET['busqueda_productos']
        producto = models.productos.objects.filter(
            Q(name__icontains=name) |
            Q(marca__name__icontains = name) |
            Q(unidad__name__icontains = name) |
            Q(proveedor__name__icontains = name)).distinct()
        
        print(producto)
        
        if not(producto.exists()):
            respuesta = "No existe un producto con ese nombre"
        
        return render(request, "./template/productos/productos_busqueda.html", {"resultado_productos": producto, "respuesta_busqueda":respuesta})
        
    else:
        respuesta = "No enviaste datos"
    return render(request, "./template/productos/productos_busqueda.html", {"respuesta_busqueda": respuesta})