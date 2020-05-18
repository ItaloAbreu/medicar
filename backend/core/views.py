from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
import rest_framework_filters as filters
from core.models import Especialidade
from core.serializers import EspecialidadeSerializer

class EspecialidadeFilter(filters.FilterSet):
    
    class Meta:
        model = Especialidade
        fields = ['nome']

class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('nome',)
    filter_class = EspecialidadeFilter
