from django.contrib import admin
from core.models import Especialidade
from core.models import Medico

class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ['nome']


class MedicoAdmin(admin.ModelAdmin):
    list_display = ['crm', 'nome', 'email', 'especialidade']

admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(Medico, MedicoAdmin)
