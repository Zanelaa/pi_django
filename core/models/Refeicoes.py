from django.db import models

from core.models.Alimentos import Alimento
from core.models.Cardapio import Cardapio


class Refeicoes(models.Model):
    nome_refeicao = models.CharField(max_length=50)
    alimentos = models.ManyToManyField(Alimento, related_name="alimentos")
    cardapios = models.ForeignKey(Cardapio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome_refeicao}"
