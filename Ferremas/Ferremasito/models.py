from django.db import models

# Modelo para representar categorías de productos en la ferretería
class Categoria(models.Model):
    # Nombre único para la categoría (ej: "Herramientas", "Electricidad")
    nombre = models.CharField(max_length=50, unique=True)

    # Relación opcional con una categoría padre (para subcategorías)
    parent = models.ForeignKey(
        'self',  # Se refiere a sí mismo (auto-relación)
        blank=True,  # No es obligatorio
        null=True,   # Puede ser nulo
        related_name='subcategorias',  # Permite acceder a las subcategorías desde una categoría padre
        on_delete=models.CASCADE  # Si se elimina la categoría padre, también se eliminan las hijas
    )

    def __str__(self):
        # Representación legible en el admin: si es subcategoría, muestra "Padre > Hijo"
        return self.nombre if not self.parent else f"{self.parent} > {self.nombre}"


# Modelo para representar los productos que se venden en Ferremas
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)  # Aquí se guardan las imágenes
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE  # Si se elimina la categoría, se eliminan también sus productos
    )

    def __str__(self):
        # Muestra el nombre del producto en interfaces administrativas
        return self.nombre
