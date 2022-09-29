from django.db import models

class Alimento(models.Model):
    titulo = models.CharField(max_length=255)
    Quantcalorias = models.CharField(max_length=32)
    quantpeso = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.titulo} ({self.Quantcalorias}) - {self.quantpeso}'