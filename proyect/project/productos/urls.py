from django.urls import path

from . import views

urlpatterns = [
    path("list", views.productoList.as_view(), name="producto_list"),
    path("nuevo", views.productoCreate.as_view(), name="producto_create"),
    path("detalle/<int:pk>", views.productodetalle.as_view(), name="producto_detail"),
    path("actualizar/<int:pk>", views.productoUpdate.as_view(), name="producto_update"),
    path("borrar/<int:pk>", views.productoDelete.as_view(), name="producto_delete"),
    
]