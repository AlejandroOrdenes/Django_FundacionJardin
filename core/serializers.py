from numpy import require, source
from .models import Categoria, Producto
from rest_framework import serializers


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    # nombre_categoria = serializers.CharField(read_only=True, source="categoria.nombreCategoria")
    categoria = CategoriaSerializer(read_only=True)
    id_categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), source="categoria")
    nombre_prod = serializers.CharField(required=True, min_length=4)

    def validate_nombre(self, value):
        existe = Producto.objects.filter(nombre_prod__iexact=value).exists()

        if existe:
            raise serializers.ValidationError("Este producto ya existe")

        return value

    class Meta:
        model = Producto
        fields = '__all__'


