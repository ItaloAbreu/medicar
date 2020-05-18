from rest_framework import serializers
from core.models import Especialidade
from core.models import Medico

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
