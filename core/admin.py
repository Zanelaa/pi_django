from django.contrib import admin

from core.models import Cardapio, Refeicoes,Alimento

admin.site.register(Refeicoes)
admin.site.register(Alimento)
admin.site.register(Cardapio)

# Register your models here.
