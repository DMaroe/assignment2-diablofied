from gc import is_finalized
import imp
from pyexpat import model
from turtle import title
from django.db import models
from django.contrib.auth.models import User
# ref : https://www.youtube.com/watch?v=zJWhizYFKP0

# Create your models here.
class Tasks(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    # ref : https://docs.djangoproject.com/en/4.1/ref/models/fields/ 
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)