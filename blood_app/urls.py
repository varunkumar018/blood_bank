from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DonorDetailsViewSet, PatientDetailViewSet, RequestViewSet, StockViewSet, FeedbackViewSet

router = DefaultRouter()
router.register(r'donor', DonorDetailsViewSet, basename='donor')
router.register(r'patient', PatientDetailViewSet, basename='patient')
router.register(r'request', RequestViewSet, basename='request')
router.register(r'stock', StockViewSet, basename='stock')
router.register(r'feedback', FeedbackViewSet, basename='feedback')

urlpatterns = [
    path('', include(router.urls)),
]
