from rest_framework import serializers
#
from .models import Users


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'id',
            'name',
            'lastname',
            'type_document',
            'document',
            'phone',
            'email',
            'password'
        )


class RegisterUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'id',
            'name',
            'lastname',
            'type_document',
            'document',
            'phone',
            'email',
            'password'
        )


class LoginDataSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField()


class LoginTokenSerializer(serializers.Serializer):
    
    token = serializers.CharField()

class UpdateUSerSerializer(serializers.Serializer):
    
    name = serializers.CharField()
    lastname = serializers.CharField()
    type_document = serializers.CharField()
    document = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.CharField()
    id_speciality = serializers.IntegerField()
