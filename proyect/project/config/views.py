from django.http import HttpResponse

from django.shortcuts import render
from django.template import Template, Context

def hola(request):
    return HttpResponse('hola')

def productos(request):
    my_html = open("./template/home.html", encoding="utf8")
    my_template = Template(my_html.read())
    my_html.close()
    my_document = my_template.render(Context())
    return HttpResponse(my_document)

def prueba_variables(request):
    name= "Leandro"
    surname= "Garro"
    datos= {"name": name, "surname": surname}
    return render(request, "prueba_variables.html", datos)

def prueba_bucles(request):
    lista_notas= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Contexto= {"notas": lista_notas}
    return render(request, "prueba_bucles.html", Contexto)
