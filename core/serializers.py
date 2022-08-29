from rest_framework.serializers import ModelSerializer

from core.models import Alimento, Cardapio, Refeicaoes

class AlimentoSerializer(ModelSerializer):
    class Meta:
        model = Alimento
        fields = "__all__"

class CardapioSerializer(ModelSerializer):
    class Meta:
        model = Cardapio
        fields = "__all__"

class RefeicaoesSerializer(ModelSerializer):
    class Meta:
        model = Refeicaoes
        fields = "__all__"