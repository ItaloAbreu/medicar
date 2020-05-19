from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import serializers
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet
from django_filters.filters import Filter
from django_filters.fields import Lookup
from core.models import Especialidade
from core.models import Medico
from core.models import Agenda
from core.serializers import EspecialidadeSerializer
from core.serializers import MedicoSerializer
from core.serializers import AgendaSerializer
import django_filters


class EspecialidadeViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nome',)


class MedicoFilterSet(FilterSet):

    class Meta:
        model = Medico
        fields = ['especialidade']


class MedicoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    filter_class = MedicoFilterSet
    filterset_fields = ['especialidade']
    search_fields = ('nome',)


class AgendaFilterSet(FilterSet):
    medico = MedicoSerializer()
    medico__especialidade = django_filters.ModelChoiceFilter(
        label="Especialidade",
        to_field_name='id',
        queryset=Especialidade.objects.all())
    especialidade = medico__especialidade
    dia_inicio = django_filters.DateFilter(field_name='dia', lookup_expr='gt')
    dia_final = django_filters.DateFilter(field_name='dia', lookup_expr='lt')

    class Meta:
        model = Agenda
        fields = ['medico', 'especialidade', 'dia_inicio', 'dia_final']


class AgendaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    filter_class = AgendaFilterSet
    filterset_fields = ['medico', 'especialidade', 'dia_inicio', 'dia_final']
    search_fields = ('medico', 'especialidade', 'dia_inicio', 'dia_final',)
