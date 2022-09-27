from pickletools import decimalnl_long
from unicodedata import decimal
from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    login = models.CharField(max_length=16, unique=True)
    email = models.CharField(null=False)
    senha = models.CharField(max_length=8, null=False)

class Refeicaoes(models.Model):
    tituloref = models.CharField(max_length=200) 
    def __str__(self):
        return self.tituloref
        
class Alimento(models.Model):
    titulo = models.CharField(max_length=255)
    Quantcalorias = models.CharField(max_length=32)
    quantpeso = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.titulo} ({self.Quantcalorias}) - {self.quantpeso}'

class Cardapio(models.Model):
    titulocard = models.CharField(max_length=255)
    numerorefs = models.CharField(max_length=2)
    refeicoes = models.ManyToManyField(Refeicaoes, related_name="cardapio")

    def __str__(self):
        return f'{self.titulocard} ({self.numerorefs})'

