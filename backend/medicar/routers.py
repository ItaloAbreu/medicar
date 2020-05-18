from rest_framework import routers
from core.views import EspecialidadeViewSet
from core.views import MedicoViewSet

router = routers.DefaultRouter()
router.register(r'especialidades', EspecialidadeViewSet)
router.register(r'medicos', MedicoViewSet)
