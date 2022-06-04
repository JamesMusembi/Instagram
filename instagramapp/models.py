from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    profile = models.ImageField(upload_to = 'images/',null=True)
    bio = models.CharField(max_length =60)
    username = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()    
        
    def update_profile(self):
        self.update()

    def delete_profile(self):
        self.delete()
        
    @classmethod
    def search_user(cls,search_term):
        profiles = cls.objects.filter(username__username__icontains=search_term)
        return profiles 
    