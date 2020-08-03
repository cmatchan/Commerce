from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listings(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=64)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=12, decimal_places=2)
    image_url = models.CharField(max_length=64)
    category = models.CharField(max_length=64)

class Bids(models.Model):
    pass

class Comments(models.Model):
    pass

class Category(models.Model):
    pass
