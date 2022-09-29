from rest_framework.serializers import ModelSerializer

from core.models import Alimento

class AlimentoSerializer(ModelSerializer):
    class Meta:
        model = Alimento
        fields = "__all__"