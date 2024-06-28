from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CanchaViewSet, DisponibilidadViewSet, ReservaViewSet, PagoViewSet, UserViewSet

router = DefaultRouter()
router.register('canchas', CanchaViewSet)
router.register('disponibilidades', DisponibilidadViewSet)
router.register('reservas', ReservaViewSet)
router.register('pagos', PagoViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
