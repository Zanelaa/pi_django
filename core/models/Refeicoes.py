from django.db import models

class Refeicoes(models.Model):
    nome_refeicao = models.CharField(max_length=50) 
    horario_refeicao = models.DateTimeField ()

    def __str__(self):
        return self.nome_refeicao, self.horario_refeicao