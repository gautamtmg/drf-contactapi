from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=30)
    firstname= models.CharField(max_length=244)
    lastname = models.CharField(max_length=244)
    phone_number = models.CharField(max_length=20)
    contact_picture = models.URLField(null=True)
    is_favorite = models.BooleanField(default=False)
