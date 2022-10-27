from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
#
from applications.users.models import Users
from applications.cites.models import Cites
from applications.system.models import Rols
from applications.cites.serializers import *
from .serializers import (
    EmployessSerializer,
    EmployesSerializer,
    LoginEmployeeSerializer
)
from  applications.functions import (
    response_bs,
    response,
    response_login
)
from applications.system.models import Rols



class EmployeeView(viewsets.ViewSet):
    serializers_classes = EmployessSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        employess = Users.objects.filter(id_rol=2)
        serializer = EmployessSerializer(employess, many=True)
        return response(self, 200, 'success', 'Empleados', serializer)

    def create(self, request):
        serializer = EmployesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        document = serializer.data['document']
        email = serializer.data['email']
        
        employee = Users.objects.get_employee(document, email)
        if employee:
            return response_bs(self, 404, "not Found", "Empleado existente")
        
        employee = Users.objects.create_user(
            name=serializer.data['name'],
            lastname=serializer.data['lastname'],
            type_document=serializer.data['type_document'],
            document=serializer.data['document'],
            phone=serializer.data['phone'],
            email=serializer.data['email'],
            id_rol=2,
        )

        return response(self, 200, 'success', 'Empleado registrado', serializer)

    def retrieve(self, request, pk=None):
        employee = Employess.objects.get_employee_by_id(pk)
        serializer = EmployesSerializer(employee)
        return response(self, 200, 'success', 'datos del usuario', serializer)

    def update(self, request, pk=None):
        serializer = EmployesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        employee = Employess.objects.get_employee_by_id(pk)
        employee.name = serializer.data['name']
        employee.lastname = serializer.data['lastname']
        employee.type_document = serializer.data['type_document']
        employee.document = serializer.data['document']
        employee.phone = serializer.data['phone']
        employee.email = serializer.data['email']
        employee.save_base()

        return response(self, 200, 'success', 'Empleado Actualizado', serializer)

    def destroy(self, request, pk=None):
        employee = Employess.objects.get_employee_by_id(pk)
        employee.delete()
        return response_bs(self, 200, 'success', 'empleado eliminado')


class LoginEmployeeView(viewsets.ViewSet):
    serializers_classes = EmployessSerializer

    def create(self, request):
        serializer = LoginEmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        employee = Users.objects.get(email=serializer.data['email'])
        if not employee:
            return response_bs(self, 404, "not found", "El usuario no existe")

        token, created = Token.objects.get_or_create(user=employee)
        serializer = EmployesSerializer(employee)

        return response_login(self, 20, "success", "Login realizado", serializer, token.key)


class ConfirmCitesView(viewsets.ViewSet):
    serializer_class = CiteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated] 
    
    def list(self, request):
        cites = Cites.objects.all().order_by('id_status')
        serializer = CiteUpdateSerializer(cites, many=True)
        return response(self, 200, 'success', "listado de citas", serializer)

    def retrieve(self, request, pk=None):
        cite = Cites.objects.get(id=pk)
        

    def update(self, request, pk=None):
        pass