from pyexpat import model
from django.db import models

# Create your models here.
class AboutUsModels(models.Model):
    user_to_devs = models.TextField()
    ...