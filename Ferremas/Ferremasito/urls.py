# Importamos 'path' para definir rutas, y 'views' que contiene las funciones que se ejecutan cuando se accede a esas rutas
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Lista de rutas disponibles en esta aplicación Django
urlpatterns = [
    # Ruta principal - muestra la página de inicio
    path('', views.home, name='home'),

    # Página que muestra el catálogo de productos (HTML)
    path('Producto.html', views.productos_html, name='productos_html'),

    # Página para ver el contenido del carrito de compras
    path('Carrito.html', views.ver_carrito, name='ver_carrito'),

    # Ruta para iniciar sesión (muestra formulario de login)
    path('login/', views.InicioSesion, name='login'),

    # Ruta para registrar un nuevo usuario
    path('registro/', views.Registro, name='registro'),

    # Ruta para obtener el tipo de cambio CLP → USD vía JSON (para conversión de precios)
    path('api/tipo_cambio/', views.obtener_tipo_cambio, name='tipo_cambio'),

    # Ruta API para obtener todos los productos en formato JSON (útil para frontend dinámico o apps)
    path('api/productos/', views.api_productos, name='api_productos'),

    # CRUD de productos
    # Ruta para crear un nuevo producto
    path('productos/crear/', views.crear_producto, name='crear_producto'),

    # Ruta para editar un producto existente (usa su ID)
    path('productos/editar/<int:pk>/', views.editar_producto, name='editar_producto'),

    # Ruta para eliminar un producto (usa su ID)
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),

    # Funcionalidades del carrito de compras
    # Agrega un producto al carrito según su ID
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

