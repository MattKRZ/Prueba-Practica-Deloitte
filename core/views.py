from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ProductosForm
from .models import Productos, Categorias
from django.contrib import messages

# Create your views here.
def Registro(request):

    data = {
        'form': UserCreationForm
    }

    if request.method == 'GET':
        return render(request, 'core/register.html', data)
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('productos')
            except IntegrityError:
                return HttpResponse('El nombre de usuario ya existe')

        return HttpResponse('La contraseña no coincide')

def IniciarSesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('productos')
        else:
            error_message = "Nombre de usuario o contraseña incorrectos"
            return render(request, 'core/login.html', {'error_message': error_message})
    else:
        return render(request, 'core/login.html')

def CerrarSesion(request):
    logout(request)
    return redirect('home')

def Producto(request):

    filtrar_categoria = request.GET.get("Categoria")
    categorias = Categorias.objects.all()

    if filtrar_categoria and filtrar_categoria != "Categoria":
        productos = Productos.objects.filter(category_id__category=filtrar_categoria)
    else:
        productos = Productos.objects.filter()

    data = {
        "productos": productos,
        "categorias": categorias,
        "filtrar_categoria": filtrar_categoria,
    }


    return render(request, 'core/products.html', data)

def CreacionProductos(request):

    categorias = Categorias.objects.all()

    data = {
        'form': ProductosForm,
        'categorias': categorias
    }

    if request.method == 'GET':
          return render (request, 'core/create.html', data)
    else:
        try:
            formulario = ProductosForm (request.POST)
            nuevo_formulario = formulario.save(commit=False)
            nuevo_formulario.user = request.user
            nuevo_formulario.save()
            messages.success(request, 'Producto agregado')
            return redirect('productos')
        except ValueError:
            return render(request, 'core/create.html', data)

def EliminarProducto(request, id):
    producto = Productos.objects.filter(id=id)
    producto.delete()

    messages.success(request, 'Producto eliminado')
    return redirect('productos')

def ModificarProducto(request, id):
    producto = Productos.objects.get(id=id)
    categorias = Categorias.objects.all()
    return render(request, 'core/modify.html', {'producto': producto, 'categorias': categorias})

def ModificacionProducto(request):
    print(request.POST)
    nombre = request.POST['producto']
    descripcion = request.POST['description']
    img = request.POST['img_url']
    price = request.POST['price']
    category = request.POST['categoria']
    id = request.POST["id"]

    Productos.objects.filter(pk=id).update(id=id, product_name=nombre, description=descripcion, image_url = img, price = price, category_id = category)
    return redirect('productos')

def CrearCategoria(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        nueva_categoria = Categorias(category=nombre)
        nueva_categoria.save()
        return redirect('crearCategoria')
    
    return render(request, 'core/createCategory.html')


def EliminarCategoria(request, id):
    categoria = Categorias.objects.filter(id=id)
    categoria.delete()

    messages.success(request, 'Categoria eliminada')
    return redirect('productos')

def Home(request):
    return render(request, 'core/home.html')
