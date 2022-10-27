from django.contrib import admin
from .models import (
    Rols,
    Specialitys,
    Doctors,
    Status,
    Notifications
)

# Register your models here.
admin.site.register(Rols)
admin.site.register(Specialitys)
admin.site.register(Doctors)
admin.site.register(Status)
admin.site.register(Notifications)