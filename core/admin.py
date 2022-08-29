from django.contrib import admin

from core.models import Cardapio, Refeicaoes,Alimento

admin.site.register(Refeicaoes)
admin.site.register(Alimento)
admin.site.register(Cardapio)

# Register your models here.
