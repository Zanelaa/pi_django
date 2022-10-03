from django.db import models

from core.models.Refeicoes import Refeicoes

class Cardapio(models.Model):
    titulo_card = models.CharField(max_length=25)
    comentario = models.CharField(max_length=255)
    refeiçoes = models.ManyToManyField(Refeicoes, related_name="refeiçoes")

    def __str__(self):
        return f'{self.titulo_card} ({self.comentario})'
        