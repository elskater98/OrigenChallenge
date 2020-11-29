from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.EditSession)
admin.site.register(models.EditSessionAllowed)