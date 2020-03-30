from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic

from .models import User, Profile

class UserView(generic.DetailView):
    model = User
    template_name = 'users/user.html'

class ProfileView(generic.DetailView):
    model = User
    template_name = 'profile/profile.html'

class IndexView(generic.ListView):
    template_name = 'users/index.html'
    queryset = User.objects.all()
    context_object_name = 'users'

