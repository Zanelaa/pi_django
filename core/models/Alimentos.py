from unittest.util import _MAX_LENGTH
from django.db import models

class Alimento(models.Model):
    nome_alimento = models.CharField(max_length=25)
    quant_carbo = models.IntegerField()
    quant_gordura = models.IntegerField()
    calorias = models.IntegerField()
    quant_proteina = models.IntegerField ()
    peso_p_porcao = models.IntegerField ()


    def __str__(self):
        return f'{self.nome_alimento} ({self.quant_carbo}) {self.quant_gordura} {self.calorias} {self.quant_proteina} {self.peso_p_porcao}   '