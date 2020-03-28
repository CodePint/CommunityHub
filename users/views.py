from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic

from .models import User, Profile

class UserView(generic.DetailView):
    model = User
    template_name = 'users/user.html'

class IndexView(generic.ListView):
    model = User
    template_name = 'users/index.html'

class ProfileView(generic.DetailView):
    model = User
    template_name = 'profile/profile.html'