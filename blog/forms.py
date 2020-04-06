from django.db import models
from django import forms

from users.models import User
from .models import Post

class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']
