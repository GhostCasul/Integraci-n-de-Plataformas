# Importaciones necesarias para las vistas
from django.shortcuts import render, redirect, get_object_or_404  # Funciones para renderizar plantillas, redirigir y obtener objetos
from django.views.decorators.http import require_POST  # Decorador para permitir solo métodos POST
from django.http import JsonResponse  # Permite devolver respuestas JSON, útil para APIs
import requests  # Librería externa para realizar solicitudes HTTP a APIs externas

from .models import Producto  # Modelo que representa un producto en la base de datos
from .forms import ProductoForm  # Formulario basado en el modelo Producto
from django.views.decorators.http import require_GET
from django.conf import settings

def home(request):
    # Página principal del sitio Ferremas
    return render(request, 'Ferremasito/Home.html')

def InicioSesion(request):
    # Página para que los usuarios inicien sesión
    return render(request, 'Ferremasito/InicioSesion.html')

def Registro(request):
    # Página para registrar nuevos usuarios
    return render(request, 'Ferremasito/Registro.html')

def productos_html(request):
    # Página que muestra la lista de productos en HTML
    return render(request, 'Ferremasito/Producto.html')


@require_GET
def api_productos(request):
    productos = Producto.objects.all()

    data = [
        {
            'id': p.id,
            'nombre': p.nombre,
            'descripcion': p.descripcion,
            'precio': float(p.precio),
            'stock': p.stock,
            'imagen_url': f"{settings.MEDIA_URL}{p.imagen}" if p.imagen else None,
        }
        for p in productos
    ]

    return JsonResponse({'productos': data})



def obtener_tipo_cambio_interno():
    # Intenta obtener el tipo de cambio desde una API externa (CLP a USD)
    try:
        response = requests.get("https://open.er-api.com/v6/latest/CLP", timeout=5)
        data = response.json()
        tipo_cambio_usd = data['rates']['USD']
    except Exception:
        # Si falla, usa un valor de respaldo por defecto
        tipo_cambio_usd = 0.0013
    return tipo_cambio_usd


def crear_producto(request):
    # Muestra un formulario para crear un nuevo producto
    form = ProductoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # Guarda el producto en la base de datos si el formulario es válido
        form.save()
        return redirect('lista_productos')
    return render(request, 'Ferremasito/productos/formulario.html', {'form': form})


def editar_producto(request, pk):
    # Carga un producto existente según su id (pk)
    producto = get_object_or_404(Producto, pk=pk)
    # Muestra un formulario para editar el producto
    form = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if form.is_valid():
        form.save()
        return redirect('lista_productos')
    return render(request, 'Ferremasito/productos/formulario.html', {'form': form})


def eliminar_producto(request, pk):
    # Elimina un producto de la base de datos
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('lista_productos')


def agregar_al_carrito(request, producto_id):
    # Agrega un producto al carrito usando su ID
    producto = get_object_or_404(Producto, id=producto_id)
    cantidad = int(request.POST.get('cantidad', 1))  # Cantidad que el usuario quiere agregar

    # Asegura que no se agregue más de lo que hay en stock
    if cantidad > producto.stock:
        cantidad = producto.stock

    carrito = request.session.get('carrito', {})  # Obtiene el carrito desde la sesión

    if str(producto_id) in carrito:
        # Si el producto ya está en el carrito, se suma la cantidad
        nueva_cantidad = carrito[str(producto_id)]['cantidad'] + cantidad
        carrito[str(producto_id)]['cantidad'] = min(nueva_cantidad, producto.stock)
    else:
        # Si no está, se agrega al carrito
        carrito[str(producto_id)] = {
            'nombre': producto.nombre,
            'precio': float(producto.precio),
            'cantidad': cantidad,
        }

    request.session['carrito'] = carrito  # Guarda el carrito actualizado en la sesión
    return redirect('ver_carrito')

def ver_carrito(request):
    # Muestra el contenido actual del carrito
    carrito = request.session.get('carrito', {})
    total = sum(item['precio'] * item['cantidad'] for item in carrito.values())  # Calcula el total

    items = []
    for id, item in carrito.items():
        items.append({
            'producto_id': id,
            'producto': item,
            'cantidad': item['cantidad'],
            'total': item['precio'] * item['cantidad']
        })

    tipo_cambio = obtener_tipo_cambio_interno()  # Obtiene el tipo de cambio CLP → USD

    return render(request, 'Ferremasito/Carrito.html', {
        'carrito': items,
        'total': total,
        'tipo_cambio': tipo_cambio,
    })


@require_POST
def eliminar_del_carrito(request, producto_id):
    # Elimina un producto del carrito
    carrito = request.session.get('carrito', {})
    producto_id_str = str(producto_id)
    if producto_id_str in carrito:
        del carrito[producto_id_str]
        request.session['carrito'] = carrito  # Guarda los cambios
    return redirect('ver_carrito')


def obtener_tipo_cambio(request):
    # Devuelve el tipo de cambio CLP a USD como JSON
    try:
        response = requests.get("https://open.er-api.com/v6/latest/CLP", timeout=5)
        data = response.json()
        tipo_cambio_usd = data['rates']['USD']
    except Exception:
        tipo_cambio_usd = 0.0013
    return JsonResponse({'tipo_cambio': tipo_cambio_usd})

def tipo_cambio(request):
    # Hace lo mismo que la función anterior, es redundante
    try:
        response = requests.get("https://open.er-api.com/v6/latest/CLP", timeout=5)
        data = response.json()
        tipo_cambio_usd = data['rates']['USD']
    except Exception:
        tipo_cambio_usd = 0.0013
    return JsonResponse({'tipo_cambio': tipo_cambio_usd})
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})