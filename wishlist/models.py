from django.db import models

# Create your models here.
class ItemWishlist(models.Model):
    item_name = models.CharField(max_length=255)
    item_price = models.IntegerField()
    description = models.TextField()
    is_hidden = models.BooleanField(default=False)