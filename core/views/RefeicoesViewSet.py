from rest_framework.viewsets import ModelViewSet

from core.models import Refeicoes
from core.serializers import RefeicoesSerializer

class RefeicoesViewSet(ModelViewSet):
    queryset = Refeicoes.objects.all()
    serializer_class = RefeicoesSerializer