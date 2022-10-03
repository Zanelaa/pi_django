from django.db import models

from core.models.Alimentos import Alimento

class Refeicoes(models.Model):
    nome_refeicao = models.CharField(max_length=50) 
    horario_refeicao = models.DateTimeField ()
    alimentos = models.ManyToManyField(Alimento, related_name="alimentos")

    def __str__(self):
        return f"{self.nome_refeicao} ({self.horario_refeicao})"