from rest_framework.serializers import ModelSerializer

from core.models import Refeicoes

class RefeicoesSerializer(ModelSerializer):
    class Meta:
        model = Refeicoes
        fields = "__all__"