# Importa el módulo serializers de Django REST Framework, que permite convertir
# modelos Django a formatos JSON (y viceversa) para APIs RESTful
from rest_framework import serializers

# Importa el modelo Productos desde el archivo models.py
from .models import Productos

# Define un serializador para el modelo Productos
class ProductosSerializer(serializers.ModelSerializer):
    # Clase interna Meta que configura el serializador
    class Meta:
        model = Productos  # Especifica que este serializador está basado en el modelo Productos
        fields = "__all__"  # Indica que se deben incluir todos los campos del modelo en la serialización
