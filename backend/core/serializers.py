from rest_framework import serializers
from core.models import Especialidade
from core.models import Medico
from core.models import Agenda


class EspecialidadeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Especialidade
        fields = '__all__'


class MedicoSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    especialidade = EspecialidadeSerializer()

    class Meta:
        model = Medico
        fields = ['id', 'crm', 'nome', 'especialidade']


class AgendaSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    medico = MedicoSerializer()
    horarios = serializers.ListField(child=serializers.TimeField())

    class Meta:
        model = Agenda
        fields = ['id', 'medico', 'dia', 'horarios']
