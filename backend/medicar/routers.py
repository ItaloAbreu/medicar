from rest_framework import routers
from core.views import EspecialidadeViewSet
from core.views import MedicoViewSet
from core.views import AgendaViewSet

router = routers.DefaultRouter()
router.register(r'especialidades', EspecialidadeViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'agendas', AgendaViewSet)
