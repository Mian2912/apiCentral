from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#
from django.utils import timezone
#
from .models import Specialitys, Doctors
from .serializers import (
    SpecialitysSerializer,
    CreateSpecialitysSerializer,
    DoctorsSerializer
)
from applications.functions import response, response_bs

class SpecialitysView(viewsets.ViewSet):

    serializer_class = SpecialitysSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes= [IsAuthenticated]

    def list(self, request):
        print(request.user)
        speciality = Specialitys.objects.all()
        serializer = SpecialitysSerializer(speciality, many=True)
        return response(self, 202, 'success', 'speciality', serializer)


    def create(self, request):
        serializer = CreateSpecialitysSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        speciality = Specialitys.objects.filter(
            specialitys__icontains=serializer.data['specialitys']
        )

        if speciality:
            return response_bs(self, '400', 'error', 'La especialidad ya se encuentra registrada')

        speciality = Specialitys(
            specialitys=serializer.data['specialitys']
        )
        speciality.save(self)

        serializer = SpecialitysSerializer(speciality)
        return response(self, 200, 'success', 'Especialidad Creada', serializer)


    def retrieve(self, request, pk=None):
        specialitys = Specialitys.objects.get(id=pk)
        serializer = SpecialitysSerializer(specialitys)
        return response(self, 200, 'success', 'Speciality by id', serializer)


    def update(self, request, pk=None):
        serializer = CreateSpecialitysSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        speciality = Specialitys.objects.get(id=pk)
        speciality.specialitys = serializer.data['specialitys']
        speciality.save_base(self)

        serializer = SpecialitysSerializer(speciality)
        return response(self, 200, 'success', 'Especialidad Actualizada', serializer)


    def destroy(self, request, pk=None):
        serializer = CreateSpecialitysSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        speciality = Specialitys.objects.get(id=pk)
        speciality.delete()

        return response(self, 200, 'success', 'Especialidad eliminada', serializer)


class DoctorsView(viewsets.ViewSet):

    serializer_class = DoctorsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def list(self, request):
        doctors = Doctors.objects.all()
        serializer = DoctorsSerializer(doctors, many=True)
        return response(self, 200, "success", "listado de doctores", serializer)

    def create(self, request):
        serializer = DoctorsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        speciality = Specialitys.objects.get(id=serializer.data['id_speciality'])

        doctor = Doctors(
            name=serializer.data['name'],
            lastname=serializer.data['lastname'],
            phone=serializer.data['phone'],
            id_speciality=speciality
        ).save(self)

        return response(self, 200, "success", "medico regitrado", serializer)

    def retrieve(self, request, pk=None):
        doctor = Doctors.objects.get(id=pk)
        serializer = DoctorsSerializer(doctor)
        return response(self, 200, "success", "Datos del Medico", serializer)

    def update(self, request, pk=None):
        serializer = DoctorsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        speciality = Specialitys.objects.get(pk=serializer.data['id_speciality'])
        print(speciality)

        doctor = Doctors.objects.get(id=pk)
        doctor.name=serializer.data['name']
        doctor.lastname=serializer.data['lastname']
        doctor.phone=serializer.data['phone']
        doctor.id_speciality=speciality
        doctor.save_base()

        return response(self, 200, "success", "datos del medico actualizados", serializer) 

    def destroy(self, request, pk=None):
        serializer = DoctorsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        doctors = Doctors.objects.get(id=pk).delete()
        return response(self, 200, "success", "datos del medico eliminados", serializer)
