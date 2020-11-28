from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EditSession(models.Model):
    session_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class EditSessionAllowed(models.Model):
    session_id = models.ForeignKey(EditSession, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)