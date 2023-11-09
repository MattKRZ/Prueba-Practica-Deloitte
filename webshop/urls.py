"""
URL configuration for webshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('registro/', views.Registro, name='registro'),
    path('productos/', views.Producto, name='productos'),
    path('productos/crear', views.CreacionProductos, name="crearProducto"),
    path('productos/eliminar/<int:id>', views.EliminarProducto, name="eliminarProducto"),
    path('productos/modificar/<int:id>', views.ModificarProducto, name='modificarProducto'),
    path('productos/modificacion', views.ModificacionProducto, name="modificacionProducto"),
    path('iniciarsesion/', views.IniciarSesion, name='iniciarSesion'),
    path('categoria/crear', views.CrearCategoria, name="crearCategoria"),
    path('categoria/eliminar/<int:id>', views.EliminarCategoria, name="eliminarCategoria"),
    path('cerrarsesion/', views.CerrarSesion, name='cerrarSesion')
]
