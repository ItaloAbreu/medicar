from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Especialidade
from core.models import Medico
from core.serializers import EspecialidadeSerializer
from core.serializers import MedicoSerializer


class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nome',)


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    filterset_fields = ['especialidade']
    search_fields = ('nome',)
