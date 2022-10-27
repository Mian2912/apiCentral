from rest_framework.routers import DefaultRouter
from .viewsets import SpecialitysView, DoctorsView

app_name = 'system'

routers = DefaultRouter()

routers.register(r'api/admin/speciality', SpecialitysView, basename='speciality')
routers.register(r'api/admin/doctors', DoctorsView, basename='doctors')

urlpatterns = routers.urls