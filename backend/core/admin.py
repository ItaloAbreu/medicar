from django.contrib import admin
from core.models import Especialidade
from core.models import Medico
from core.models import Agenda
from core.serializers import AgendaSerializer


class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ['nome']


class MedicoAdmin(admin.ModelAdmin):
    list_display = ['crm', 'nome', 'email', 'especialidade']


class AgendaAdmin(admin.ModelAdmin):
    list_display = ['medico', 'dia', 'horarios']


admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Agenda, AgendaAdmin)
