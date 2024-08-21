from django.db import models

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Autor(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    publicado_em = models.DateField()

    def __str__(self):
        return self.titulo
