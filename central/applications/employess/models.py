from model_utils.models import TimeStampedModel
#
from django.db import models
#
from applications.system.models import Rols
from .managers import EmployeeManager

# Create your models here.
class Employess(TimeStampedModel, models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    type_document = models.CharField(max_length=30)
    document = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=60, unique=True)
    password = models.CharField(max_length=100, null=True)
    id_rol = models.ForeignKey(Rols, on_delete=models.CASCADE, default=None)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = EmployeeManager()

    def __str__(self):
        return self.name
