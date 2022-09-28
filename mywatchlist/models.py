from django.db import models

#import MaxValuevalidator and MinVa
from django.core.validators import MaxValueValidator, MinValueValidator

class MyWatchListItem(models.Model):

    watched = models.BooleanField() #watched = 1, not = 0
    title = models.CharField(max_length=255) #maximum string length is 255
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) #min value is 1, max value is 5
    release_date = models.CharField(max_length=255)
    review = models.TextField() #textfield can contain more than 255 characters
    