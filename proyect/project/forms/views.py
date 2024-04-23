from django.shortcuts import render

from django.http import HttpResponse
from . import models
from . import forms

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
    
def form_proveedor_resived(request):    
    if request.method == "POST":
        my_form= forms.form_del_proveedor(request.POST, request.FILES)
    
        print(my_form)
    
        if my_form.is_valid():
            my_form.save()
            
            print("success")
            
            proveedor = models.proveedor.objects.all()
            return render(request, "./template/leer_proveedores.html", {"proveedor": proveedor})
    
    else:
        print("fail")
        my_form= forms.form_del_proveedor()
        
    return render(request, "./template/form_proveedor.html", {"my_form": my_form})


def busqueda_proveedor(request):
    return render(request, "./template/busqueda_proveedor.html")

def buscar(request):
    if request.GET['buscar_proveedor']:
        name = request.GET['buscar_proveedor']
        proveedor = models.proveedor.objects.filter(name__icontains=name)
        
        return render(request, "./template/busqueda_proveedor.html", {"proveedor": proveedor})
        
    else:
        respuesta = "No enviaste datos"    
    
    return render(request, "./template/busqueda_proveedor.html", {"respuesta": respuesta})


def leer_proveedor(request):
    proveedor = models.proveedor.objects.all()
    return render(request, "./template/leer_proveedores.html", {"proveedor": proveedor})

def borrar_proveedor(request, id):
    proveedor = models.proveedor.objects.get(id=id)
    proveedor.delete()
    
    proveedor = models.proveedor.objects.all()
    return render(request, "./template/leer_proveedores.html", {"proveedor": proveedor})


def actualizar_proveedor(request, id):
    proveedor = models.proveedor.objects.get(id=id)
    
    if request.method == "POST":
        my_form = forms.form_del_proveedor(request.POST, request.FILES, instance=proveedor)
        
        if my_form.is_valid():
            my_form.save()
            
            proveedor = models.proveedor.objects.all()
            
            return render(request, "./template/leer_proveedores.html", {"proveedor": proveedor})

    else:
        my_form = forms.form_del_proveedor(instance=proveedor)
    
    return render(request, "./template/actualizar_proveedor.html", {"proveedor": proveedor, "my_form": my_form})


class proveedorList(ListView):
    model = models.proveedor
    template_name = "forms/templates/forms/leer_proveedores.html"
    context_object_name = "proveedor"
    
class proveedordetalle(DetailView):
    model = models.proveedor
    template_name = "forms/template/leer_proveedores.html"
    context_object_name = "proveedor"
    
class proveedorCreate(CreateView):
    model = models.proveedor
    template_name = "project/template/form_proveedor.html"
    fields = ["name", "surname", "email", "phone", "country", "provee"]
    success_url = reverse_lazy("leer_proveedor")
    
class proveedorUpdate(UpdateView):
    model = models.proveedor
    success_url = "/proveedor/list"
    fields = ["name", "surname", "email", "phone", "country", "provee"]
    
class proveedorDelete(DeleteView):
    model = models.proveedor
    success_url = reverse_lazy("leer_proveedor")
    

    
