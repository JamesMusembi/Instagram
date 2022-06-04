from django.test import TestCase
from . models import Image, Profile, Comments

# Create your tests here.


class ImageTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.butterfly= Image(image = 'book.jpg', name ='butterfly', caption ='about butterfly')
        self.pizza= Image(image = 'piza.jpg', name ='pizza', caption ='about pizza')
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.butterfly,Image))        
        
        # Testing Save Method of Image model
    def test_save_method(self):
        self.butterfly.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)  
        
    # Testing  delete method of Image model     
    def test_delete(self):
        self.pizza= Image(image = 'piza.jpg', name ='pizza', caption ='about pizza')
        self.pizza.save_image()
        image = Image.objects.filter(name = 'pizza').first()
        delete = Image.objects.filter(id = image.id).delete()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)    
        
    # Testing  update method of Image model    
    def test_update(self):
        self.pizza.save_image()
        image = Image.objects.filter(name = 'pizza').first()
        update = Image.objects.filter(id = image.id).update(name = 'cake')
        updated = Image.objects.filter(name = 'cake').first()
        self.assertNotEqual(image.name, updated.name) 
        
# Profile model test  
      
class ProfileTestClass(TestCase):        
    
        # Set up method
    def setUp(self):
        self.image= Profile(profile = 'img.jpg', bio ='image')
        # self.images= Profile(profile1 = 'piza1.jpg', bio ='pizza')
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Profile))     
        
        # Testing Save Method of Profile model
    def test_save_method(self):
        self.image.save_profile()
        images = Profile.objects.all()
        self.assertTrue(len(images) > 0)         
        
    # Testing  delete method of Profile model     
    def test_delete(self):
        self.image= Profile(profile = 'img.jpg', bio ='image')
        self.image.save_profile()
        image = Profile.objects.filter(profile = 'img.jpg').first()
        delete = Profile.objects.filter(id = image.id).delete()
        images = Profile.objects.all()
        self.assertTrue(len(images) == 0)            
        
    # Testing  update method of Profile model    
    def test_update(self):
        self.image.save_profile()
        image = Profile.objects.filter(profile = 'img.jpg').first()
        update = Profile.objects.filter(id = image.id).update(profile = 'cake.jpg')
        updated = Profile.objects.filter(profile = 'cake.jpg').first()
        self.assertNotEqual(image.profile, updated.profile)  
        
