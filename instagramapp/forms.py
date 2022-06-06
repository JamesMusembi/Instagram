from django import forms
from .models import Image, Profile,Comments

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['comment', 'profile','name']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = []        