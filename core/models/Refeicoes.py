from django.db import models

class Refeicoes(models.Model):
    tituloref = models.CharField(max_length=50) 
    def __str__(self):
        return self.tituloref