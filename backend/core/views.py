from rest_framework import viewsets
from rest_framework import filters
from core.models import Especialidade
from core.serializers import EspecialidadeSerializer

class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nome',)
