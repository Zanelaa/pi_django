from rest_framework.viewsets import ModelViewSet

from core.models import Alimento
from core.serializers import AlimentoSerializer

class AlimentoViewSet(ModelViewSet):
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer