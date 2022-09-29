from django.db import models

class Cardapio(models.Model):
    titulocard = models.CharField(max_length=255)
    numerorefs = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.titulocard} ({self.numerorefs})'