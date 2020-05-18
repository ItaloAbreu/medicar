from rest_framework import serializers
from core.models import Especialidade

class EspecialidadeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Especialidade
        fields = '__all__'
    