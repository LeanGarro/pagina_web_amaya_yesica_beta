from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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
    
class busqueda_productos(View):
    """ muestra la vista de busqueda de proveedor """
    def get(self, request):
        return render(request, "./template/productos/busqueda_productos.html")

    def post(self, request):
        return render(request, "./template/productos/busqueda_productos.html")
    