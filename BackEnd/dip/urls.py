from django.urls import path, include
from rest_framework import routers
from patients.viewsets import PatientViewSet

router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patients')

urlpatterns = [
    path('', include(router.urls)),
]
