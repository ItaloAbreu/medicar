from django.contrib import admin
from core.models import Especialidade

class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ['nome']

admin.site.register(Especialidade, EspecialidadeAdmin)
