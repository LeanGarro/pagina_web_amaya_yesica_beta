from django.urls import path

from . import views

urlpatterns = [
    path('form_proveedor/', views.form_proveedor_resived, name='form_proveedor'),
    path('busqueda_proveedor/', views.busqueda_proveedor, name='busqueda_proveedor'),
    path('buscar/', views.buscar),
    path("leer_proveedor/", views.leer_proveedor),
    path("eliminar_proveedor/<int:id>/", views.borrar_proveedor, name="Borrar_Proveedor"),
    path("actualizar_proveedor/<int:id>/", views.actualizar_proveedor, name="Actualizar_Proveedor"),
    
    
    path("proveedor/list", views.proveedorList.as_view(), name="proveedor_list"),
    path("proveedor/<int:pk>", views.proveedordetalle.as_view(), name="proveedor_detalle"),
    path("proveedor/nuevo", views.proveedorCreate.as_view(), name="proveedor_create"),
    path("proveedor/actualizar/<int:pk>", views.proveedorUpdate.as_view(), name="proveedor_update"),
    path("proveedor/borrar/<int:pk>", views.proveedorDelete.as_view(), name="proveedor_delete"),
]