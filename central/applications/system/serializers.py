from rest_framework import serializers
from .models import Specialitys, Doctors

class SpecialitysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialitys
        fields = (
            'id',
            'specialitys'
        )


class CreateSpecialitysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialitys
        fields = (
            'specialitys',
        )

class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ('__all__')