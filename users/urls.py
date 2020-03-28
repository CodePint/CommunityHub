from django.contrib import admin
from django.urls import include
from django.urls import path
from . import views

# slug is set to username
urlpatterns = [
    path('', include('allauth.urls')),
    path('user/<slug:slug>', views.UserView.as_view(), name='user'),
    path('user/profile/<slug:slug>', views.ProfileView.as_view(), name='profile'),
    path('users/', views.IndexView.as_view(), name='users'),
]