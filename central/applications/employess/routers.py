from rest_framework.routers import DefaultRouter
#
from .viewsets import (
    EmployeeView,
    LoginEmployeeView,
    UpdateCitesView
)

routers = DefaultRouter()

routers.register(r'api/admin/employee', EmployeeView, basename='employee')
routers.register(r'api/employee/login', LoginEmployeeView, basename='employee_login')
routers.register(r'api/employes/cites', ConfirmCitesView, basename='employee_cite')

urlpatterns = routers.urls