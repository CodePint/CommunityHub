from django.db import models
from django import forms

from .models import User
from .models import HelpNotice

class CreateHelpNotice(forms.ModelForm):

    class Meta:
        model = HelpNotice
        fields = ['title', 'content']
