from django.db import models
from django import forms

from .models import User
from .models import HelpNotice

class HelpNoticeForm(forms.ModelForm):

    class Meta:
        model = HelpNotice
        fields = ['title', 'content', 'status', 'ending_at']
    
    def __init__(self, *args, created=False, **kwargs):
        super(HelpNoticeForm, self).__init__(*args, **kwargs)
        if created:
            del self.fields['status']
        else:
            self.fields['title'].disabled = True
