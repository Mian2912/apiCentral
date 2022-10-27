from django.db import models
from django.contrib.auth.models import BaseUserManager
#


class EmployeeManager(BaseUserManager, models.Manager):

    def get_employee(self, document, email):
        return self.filter(
            document=document,
            email=email
        )
 
    def get_employee_by_id(self, pk):
        return self.get(id=pk)
    