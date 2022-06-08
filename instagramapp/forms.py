from django import forms
from .models import Image, Profile,Comment

# class NewImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         exclude = ['comment', 'profile','name', 'comment', 'caption']
#         widgets = {
#             'tags': forms.CheckboxSelectMultiple(),
#         }
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['fullname','profile_img','bio','email_phone']
        
# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ('image', 'caption')