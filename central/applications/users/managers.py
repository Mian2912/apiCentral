from django.db import models
from django.contrib.auth.models import BaseUserManager
#
from applications.system.models import Rols

class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, email, password, is_staff, is_superuser, id_rol, **extra_fields):
        user = self.model(
            email=email,
            password=password,
            is_staff=is_staff,
            is_superuser = is_superuser,
            id_rol = Rols.objects.get(id=id_rol),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, id_rol=None, **extra_fields):
        return self._create_user(email, password, True, False, id_rol, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, True, True, 1, **extra_fields)


    def search_user(self, email):
        # buscar usuario por email
        return self.get(email=email)

    def get_employee(self, document, email):
        return self.filter(
            document=document,
            email=email
        )
 
    def get_employee_by_id(self, pk):
        return self.get(id=pk)
    


