from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterViewSet, CanchaViewSet, DisponibilidadViewSet, ReservaViewSet, PagoViewSet

router = DefaultRouter()
router.register(r'register', RegisterViewSet)
router.register(r'canchas', CanchaViewSet)
router.register(r'disponibilidades', DisponibilidadViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'pagos', PagoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]