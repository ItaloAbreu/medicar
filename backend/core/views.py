from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet
from django_filters.filters import Filter
from django_filters.fields import Lookup
from core.models import Especialidade
from core.models import Medico
from core.serializers import EspecialidadeSerializer
from core.serializers import MedicoSerializer


class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nome',)


class MedicoFilterSet(FilterSet):

    class Meta:
        model = Medico
        fields = ['especialidade']


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    filter_class = MedicoFilterSet
    filterset_fields = ['especialidade']
    search_fields = ('nome',)
