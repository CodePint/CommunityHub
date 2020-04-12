from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import View
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CreatePostForm
from .models import Post
from .models import User
from django.db.models import F

class BlogIndex(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        posts = Post.objects.all().order_by('-created_at')[:10]
        context = {'posts': posts, 'user': user}
        return render(request, "blog/index.html", context=context)

class BlogAuthor(View):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, username=kwargs['author'])
        posts = user.posts.all()
        context = {'author': user, 'posts': posts}
        return render(request, "blog/author.html", context=context)

class PostDetail(View):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, slug=kwargs['slug'])
        context = {'post': post}
        return render(request, "blog/detail.html", context=context)

class CreatePost(LoginRequiredMixin, View):
    login_url = '/user/login'

    def get(self, request, *args, **kwargs):
        user = request.user
        context = {'user': user, 'form': CreatePostForm()}
        return render(request, 'blog/create.html', context)

    def post(self, request, *args, **kwargs):
        user = request.user
        form = CreatePostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.status = 1
            post.save()
            return redirect(post)

        return render(request, 'blog/create.html', {'form': form})


