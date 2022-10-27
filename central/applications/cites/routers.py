from rest_framework.routers import DefaultRouter
#
from .viewsets import AddCitePerson, AddCiteFamily


routers = DefaultRouter()

routers.register(r'api/cite/citeperson', AddCitePerson, basename="citePerson")
routers.register(r'api/cite/citefamily', AddCiteFamily, basename="citeFamily")

urlpatterns = routers.urls