from rest_framework.routers import DefaultRouter

from .viewsets import (
    RegisterUserView,
    LoginUserView,
    ProfileUserView
)

routers = DefaultRouter()


routers.register(r'register', RegisterUserView ,basename='api_users')
routers.register(r'api/login', LoginUserView, basename='api_login')
routers.register(r'api/user/profile', ProfileUserView, basename='profile')

urlpatterns = routers.urls