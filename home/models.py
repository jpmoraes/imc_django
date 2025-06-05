from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria  # Para mostrar o nome no admin ou templates


class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    peso = models.IntegerField(default=000)
    altura = models.IntegerField(default=000)
    
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return (self.nome, self.peso, self.altura)

    