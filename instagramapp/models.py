from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    profile = models.ImageField(upload_to = 'images/',null=True)
    bio = models.CharField(max_length =60)
    username = models.ForeignKey(User,on_delete=models.CASCADE, null=True)