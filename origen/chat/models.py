from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EditSession(models.Model):
    session_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default='Room')
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

class EditSessionAllowed(models.Model):
    id = models.IntegerField(primary_key=True)
    session = models.ForeignKey(EditSession, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)