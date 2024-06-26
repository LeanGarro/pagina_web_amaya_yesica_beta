from django.shortcuts import render

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
    respuesta = " "
    
    """ busca un proveedor en la DB y lo muestra"""
    if request.GET['buscar_proveedor']:
        name = request.GET['buscar_proveedor']
        proveedor = models.proveedor.objects.filter(
            Q(name__icontains=name) |
            Q(email__icontains = name) |
            Q(provee__icontains = name)).distinct()
        
        print(proveedor)
        
        if not(proveedor.exists()):
            respuesta = "No existe un proveedor con ese nombre"
        
        return render(request, "./template/proveedor/busqueda_proveedor.html", {"resultado_proveedor": proveedor, "respuesta_busqueda": respuesta})
        
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
    fields = '__all__'
    success_url = reverse_lazy("proveedor_list")
    
    def form_valid(self, form):
        # Guarda el formulario y la imagen asociada
        instance = form.save(commit=False)
        instance.imagen = self.request.FILES.get('imagen')
        instance.save()
        return super().form_valid(form)
    
class proveedorUpdate(UpdateView):
    """ acrualiza un proveedor de la BD """
    model = models.proveedor
    from_class = forms.form_del_proveedor
    template_name = "proveedor/form_proveedor.html"
    fields = '__all__'
    success_url = reverse_lazy("proveedor_list")
    
class proveedorDelete(DeleteView):
    """ elimina un proveedor de la BD """
    model = models.proveedor
    template_name = "proveedor/proveedor_delete.html"
    success_url = reverse_lazy("proveedor_list")
