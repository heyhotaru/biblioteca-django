from rest_framework import serializers
from .models import Categoria, Autor, Livro

class CategoriaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Categoria.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class AutorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)


    def create(self, validated_data):
        return Autor.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class LivroSerializer(serializers.Serializer):
    id = serializers.Integerfield(read_only=True)
    titulo = serializer.CharField(max_length=200)
    autor = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all())
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    publicado_em = serializers.DateField()
    
    def create(self, validated_data):
        return Livro.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.autor = validated_data.get('autor', instance.autor)
        instance.categoria = validated_data.get('categoria', instance.categoria)
        instance.publicado_em = validated_data.get('publicado_em', instnace.publicado_em)
        instance.save()
        return instance