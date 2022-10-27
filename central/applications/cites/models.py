from model_utils.models import TimeStampedModel
#
from django.db import models
#
from applications.employess.models import Employess
from applications.users.models import Users
from applications.system.models import (
    Specialitys,
    Doctors,
    Status
)
from .managers import CiteManager

# Create your models here.
class Cites( TimeStampedModel, models.Model ):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    type_document = models.CharField(max_length=30)
    document = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    eps = models.CharField(max_length=20)
    id_speciality = models.ForeignKey(Specialitys, on_delete=models.CASCADE, default=None)
    id_doctors = models.ForeignKey(Doctors, on_delete=models.CASCADE, null=True, blank=True)
    required_files = models.CharField(max_length=30, null=False, blank=False)
    orden_file = models.FileField(null=False, blank=False)
    autorization = models.FileField(null=False, blank=False)
    id_status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, default=None)
    recommendations = models.CharField(max_length=100, null=False, blank=False)
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE, default=None)
    id_employee = models.ForeignKey(Employess, on_delete=models.CASCADE, null=True, blank=True, default=None)

    objects = CiteManager()

    def __str__(self):
        return f'{self.id} - {self.name}'