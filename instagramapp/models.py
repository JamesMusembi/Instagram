from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from tinymce.models import HTMLField
from django.db.models.signals import post_save

# Create your models here.
        
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    fullname=models.CharField(max_length=100,blank=True,null=True)
    profile_img=models.ImageField(upload_to='image/',default='static/images/nature15.jpg',null=True)
    bio=models.TextField(blank=True,null=True)
    email_phone=models.CharField(max_length=100,blank=True,null=True)
    followers=models.ManyToManyField(User,related_name='followers')
    following=models.ManyToManyField(User,related_name='following')
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self,id,profile):
        updated_profile=Profile.objects.filter(id=id).update(profile)
        return updated_profile

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            instance.profile.save()

        post_save.connect(Profile, sender=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        Profile.objects.get_or_create(user=instance)
        instance.profile.save()
     
    
class Image(models.Model):
    img_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/',null=True)
    image_caption=models.CharField(max_length=200)
    profile=models.ForeignKey(User, on_delete = models.CASCADE)
    likes=models.ManyToManyField(User,related_name='likes')
    created_at=models.DateTimeField(auto_now_add=True)
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self,id,image_caption):
        updated_caption=Image.objects.filter(id=id).update(image_caption)
        return updated_caption

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.img_name       
        
class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    img=models.ForeignKey(Image,on_delete=models.CASCADE)
    comment=models.TextField()
        
    def save_comment(self):
        self.save()
    
    def delete_comment(self):
        self.delete()

    def __str__(self):
        return self.comment
