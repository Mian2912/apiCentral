from rest_framework import serializers
#
from .models import Employess


class EmployessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employess
        fields = ('__all__')

class EmployesSerializer(serializers.Serializer):
    name = serializers.CharField()
    lastname = serializers.CharField()
    type_document = serializers.CharField()
    document = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()


class LoginEmployeeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()