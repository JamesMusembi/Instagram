from email.policy import default
# from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils import timezone


# Create your models here.
        
class Profile(models.Model):
    profile = models.ImageField(upload_to = 'images/',null=True,default='images/67.jpg')
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
    
class Image (models.Model):
    image = models.ImageField(upload_to = 'images/',null=True,default='images/66.jpg')
    name = models.CharField(max_length =40)
    caption=  HTMLField()
    comment= models.CharField(max_length =100)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,default='True')
    username = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    post_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()

    def update_image(self):
        self.update()

    def delete(self):
        self.delete()    
class Meta:
        ordering = ['post_date']        
        
class Comments(models.Model):
    image = models.ForeignKey(Image,blank=True, on_delete=models.CASCADE)
    commentator = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    comment= models.TextField()
        
