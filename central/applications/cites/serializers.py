from rest_framework import serializers
#
from applications.users.models import Users
from .models import Cites
from applications.system.models import Specialitys
#

class CiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cites
        fields = ( 
            '__all__'
        )

class CitesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cites
        fields = (
            'id',
            'name',
            'lastname',
            'type_document',
            'document',
            'required_files',
            'orden_file',
            'autorization',
            'recommendations',
            'id_speciality',
            'id_doctors',
            'id_status',
            'id_user'
        )


class CiteSerializerPerson(serializers.Serializer):
    id_speciality = serializers.IntegerField()


class CreateCiteSerializer(serializers.Serializer):
    name = serializers.CharField()
    lastname = serializers.CharField()
    type_document = serializers.CharField()
    document = serializers.CharField()
    id_speciality = serializers.IntegerField()

class CiteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cites
        fields=('__all__')
        # fields = (
        #     'id',
        #     'name',
        #     'lastname',
        #     'type_document',
        #     'document',
        #     'required_files',
        #     'orden_file',
        #     'autorization',
        #     'recommendations',
        #     'id_speciality',
        #     'id_doctors',
        #     'id_status',
        #     'id_user'
        # )
