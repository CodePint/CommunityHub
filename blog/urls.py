from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogIndex.as_view(), name='index'),
    path('<slug:author>/', views.BlogAuthor.as_view(), name='author'),
    path('<slug:author>/create/', views.CreatePost.as_view(), name='create'),
    path('<slug:author>/post/<slug:slug>/', views.PostDetail.as_view(), name='detail'),
]
