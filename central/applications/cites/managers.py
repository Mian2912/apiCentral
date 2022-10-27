from django.db import models

class CiteManager(models.Manager):

    def get_speciality(self, pk):
        return self.get(id=pk)
    
    def get_cites_user(self, user):
        return self.filter(id_user=user.id)


