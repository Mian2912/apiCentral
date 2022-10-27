from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#
from django.shortcuts import get_object_or_404
from django.utils import timezone
#
from .models import Users
from applications.system.models import Rols
from .serializers import (
    UserSerializers,
    RegisterUserSerializers,
    LoginDataSerializer,
    LoginTokenSerializer,
    UpdateUSerSerializer
)
from applications.functions import (
    response,
    response_login,
    response_bs
)
from applications.users.managers import UserManager
#

class RegisterUserView(viewsets.ViewSet):

    serializer_class = RegisterUserSerializers

    def create(self, request):

        serializer = RegisterUserSerializers(data=request.data)
        serializer.is_valid(raise_exception=False)
        
        email = serializer.data['email']
        # user = Users.objects.search_user(email)

        # # if user:
        # #     return response(self, 400, 'error', "el usuario se encuentra registrado", serializer)

        user = Users.objects.create_user(
            email=serializer.data['email'],
            password=serializer.data['password'],
            name=serializer.data['name'],
            lastname=serializer.data['lastname'],
            type_document=serializer.data['type_document'],
            document=serializer.data['document'],
            phone=serializer.data['phone'],
            id_rol=3
        )

        serializer = RegisterUserSerializers(user)

        return response(self, 200, 'success', 'usuario registrado', serializer)
        


class LoginUserView(viewsets.ViewSet):

    serializer_class = LoginTokenSerializer

    def create(self, request):

        serializer = LoginDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']
        usuario = Users.objects.search_user(email)

        if not usuario:
            return response(self, 404, 'error', 'correo y/o contraseñas son invalidas, intentalo mas tarde', serializer)

        serializer = UserSerializers(usuario)        
        token, created = Token.objects.get_or_create(user=usuario)

        return response_login(self, 200, 'success', 'login exitoso', serializer, token.key)


class ProfileUserView(viewsets.ViewSet):
    serializer_class = UpdateUSerSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def list(self, request):
        return response_bs(self, 404, 'not found', 'peticion no encontrada')

    def update(self, request, pk=None):
        serializer = UpdateUSerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        
        user = Users.objects.get(id=pk)
        user.name = data['name']
        user.lastname = data['lastname']
        user.type_document = data['type_document']
        user.document = data['document']
        user.phone = data['phone']
        user.email = data['email']
        user.modified = timezone.now()
        user.save_base(user )

        serializer = UpdateUSerSerializer(user)
        return response(self, 201, 'success', 'usuario actualizado', serializer)

    def retrieve(self, request, pk=None):
        serializer = UserSerializers(data=request.data)
        user = Users.objects.get(id=pk)
        serializer = UserSerializers(user)
        return response(self, 200, 'success', 'usuario encontrado', serializer)