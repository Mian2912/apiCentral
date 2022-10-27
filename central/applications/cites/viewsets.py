from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
#
from django.utils import timezone
#
from .models import Cites
from .serializers import (
    CiteSerializer,
    CitesSerializer,
    CreateCiteSerializer,
    CiteSerializerPerson
)
from applications.functions import (
    response_bs,
    response
)
from applications.users.models import Users
from applications.users.serializers import (
    UserSerializers
)
from applications.users.managers import UserManager
from applications.system.models import Specialitys, Status
#

class AddCitePerson(viewsets.ViewSet):
    serializer_class = CiteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes= [IsAuthenticated]

    def create(self, request):

        serializer_cite = CiteSerializerPerson(data=request.data)
        serializer_cite.is_valid(raise_exception=True)
        speciality = Specialitys.objects.get_speciality(serializer_cite.data['id_speciality'])
        user = self.request.user
        status = Status.objects.get(id=1)
        cite = Cites(
            name=user.name,
            lastname=user.lastname,
            type_document=user.type_document,
            document=user.document,
            id_speciality=speciality,
            id_status=status,
            id_user=user
        )
        cite.save(self)

        serializer_cite = CitesSerializer(cite)

        return response(self, 200, 'success', 'cita agendada', serializer_cite)


class AddCiteFamily(viewsets.ViewSet):
    serializer_class = CreateCiteSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes= [IsAuthenticated]

    def list(self, request):
        user = self.request.user
        cites = Cites.objects.get_cites_user(user)
        serializer = CitesSerializer(cites, many=True, context={'request': request})
        return response(self, 200, "success", "cites recuperados", serializer)


    def create(self, request):
        serializer_cite = CreateCiteSerializer(data=request.data)
        serializer_cite.is_valid(raise_exception=True)
        data = serializer_cite.data

        # instacia de specialidades
        speciality = Specialitys.objects.get_speciality(data['id_speciality'])

        # instancia de status
        status = Status.objects.get(id=1)

        cite= Cites(
            name=data['name'],
            lastname=data['lastname'],
            type_document=data['type_document'],
            document=data['document'],
            id_speciality= speciality,
            id_status=status,
            id_user=self.request.user
        )
        cite.save(self)

        serializer_cite = CiteSerializer(cite)

        return response(self, 202, 'success', 'cita agregada', serializer_cite)


    def retrieve(self, request, pk=None):
        cites = Cites.objects.get(id=pk)
        serializer = CitesSerializer(cites)
        return response(self, 200, 'success', 'cita recuperada', serializer)

    def update(self, request):

        pass