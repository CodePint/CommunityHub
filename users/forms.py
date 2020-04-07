from django import forms
from django.conf import settings
from .models import Profile

class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'location']
