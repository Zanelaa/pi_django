#from rest_framework.permissions import IsAuthenticated#
from rest_framework.viewsets import ModelViewSet


from core.models import Alimento,Cardapio,Refeicaoes
from core.serializers import AlimentoSerializer, CardapioSerializer,RefeicaoesSerializer

class AlimentoViewSet(ModelViewSet):
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer
    #permission_classes = [IsAuthenticated]#

class CardapioViewSet(ModelViewSet):
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializer

class RefeicaoesViewSet(ModelViewSet):
    queryset = Refeicaoes.objects.all()
    serializer_class = RefeicaoesSerializer
# Create your views here.
