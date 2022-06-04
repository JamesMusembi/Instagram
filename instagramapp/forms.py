from django import forms
from .models import Image, Profile

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['comments', 'profile','name']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = []        