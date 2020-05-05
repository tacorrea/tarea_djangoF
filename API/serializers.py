from rest_framework import serializers
from .models import Hamburguesa, Ingrediente


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id', 'nombre', 'descripcion']
    def get_queryset(self):
        return Ingrediente.objects.all() 

class IngredientePathSerializer(serializers.ModelSerializer):

    path = serializers.SerializerMethodField()
    class Meta:
        model = Ingrediente
        fields = ['path'] 
    def get_queryset(self):
        return Ingrediente.objects.all()      
    def get_path(self, ingrediente):
        return 'https://obscure-atoll-26820.herokuapp.com{}'.format(reverse('ingrediente-details', args=[ingrediente.id]))

class HamburguesaSerializer(serializers.ModelSerializer):
    ingredientes = IngredientePathSerializer(read_only=True, many=True)
    class Meta:
        model = Hamburguesa
        fields = ['id', 'nombre', 'precio', 'descripcion', 'imagen', 'ingredientes']
    def get_queryset(self):
        return Hamburguesa.objects.all() 