from model_utils.models import TimeStampedModel
#
from django.db import models
#
# from applications.users.models import Users
# from applications.cites.models import Cites
from .managers import SpecialityManager

# Create your models here.
class Rols( TimeStampedModel , models.Model ):
    rols = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.id} - {self.rols}'


class Specialitys( TimeStampedModel, models.Model ):
    specialitys = models.CharField(max_length=50)
    objects = SpecialityManager()

    def __str__(self):
        return f'{self.id} - {self.specialitys}'


class Doctors( TimeStampedModel, models.Model ):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    type_document = models.CharField(max_length=30)
    document = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    id_speciality = models.ForeignKey(Specialitys, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.name}'


class Status( TimeStampedModel, models.Model ):
    status = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.id} - {self.status}'


class Notifications( TimeStampedModel, models.Model ):
    message = models.CharField(max_length=100)
    # id_cite = models.ForeignKey(Cites, on_delete=models.CASCADE, null=True, blank=True, default=None)
    # id_user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, default=None)