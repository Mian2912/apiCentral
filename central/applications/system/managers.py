from django.db import models

class SpecialityManager(models.Manager):

    def get_speciality(self, pk):
        return self.get(id=pk)