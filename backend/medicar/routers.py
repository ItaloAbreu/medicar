from rest_framework import routers
from core.views import EspecialidadeViewSet

router = routers.DefaultRouter()
router.register(r'especialidades', EspecialidadeViewSet)
