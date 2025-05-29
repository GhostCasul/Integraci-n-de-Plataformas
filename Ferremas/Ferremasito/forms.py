# Importa el módulo de formularios de Django
from django import forms

# Importa el modelo Producto desde la app actual
from .models import Producto

# Define un formulario basado en el modelo Producto
class ProductoForm(forms.ModelForm):
    # Clase interna Meta define configuración del formulario
    class Meta:
        model = Producto  # Especifica que el formulario se basa en el modelo Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'categoria', 'imagen']
        # Estos son los campos del modelo que se incluirán en el formulario
