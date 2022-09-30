from django.db import models

class Cardapio(models.Model):
    titulo_card = models.CharField(max_length=25)
    comentario = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.titulocard} ({self.numerorefs})'