from model_utils.models import TimeStampedModel
#
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from applications.system.models import Rols
from .managers import UserManager

# Create your models here.
class Users(TimeStampedModel, AbstractBaseUser, PermissionsMixin):

    TYPE_DOCUMENT = (
        ('Cedula de ciudadania','Cedula de ciudadania'),
        ('Libreta Miliar', 'Libreta Miliar')
    ) 

    name = models.CharField(max_length=20, blank=True)
    lastname = models.CharField(max_length=20, blank=True)
    type_document = models.CharField(max_length=30, choices=TYPE_DOCUMENT, blank=True)
    document = models.CharField(max_length=20, unique=True, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    email = models.EmailField(max_length=60, unique=True)
    id_rol = models.ForeignKey(Rols, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return f'{self.id} - {self.name}'

