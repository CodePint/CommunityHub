from django.contrib import admin
from django.urls import include
from django.urls import path
from . import views

# slug is set to username
urlpatterns = [
    path('user/', include('allauth.urls')),
    path('users/', views.IndexView.as_view(), name='users'),
    path('user/<slug:slug>/', views.ProfileView.as_view(), name='profile'),
    path('user/<slug:slug>/edit', views.ProfileEdit.as_view(), name='profile_edit'),
]