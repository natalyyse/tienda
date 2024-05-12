from rest_framework import serializers
from .models import Categoria, Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'stock', 'imagen_url','pub_date', 'categoria']

class CategoriaSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True, read_only=True)

    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'pub_date', 'productos']
        