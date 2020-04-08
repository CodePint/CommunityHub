from django.shortcuts import render

#from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import View
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

# from .forms import CreatePostForm
from users.models import User
from django.db.models import F

class HelpIndex(View):
    def get(self, request, type='', *args, **kwargs):
        user = request.user
        # posts = Post.objects.all().order_by('-created_at')[:10]
        context = {'user': user, 'type': type}
        return render(request, "help/index.html", context=context)

class HelpDetail(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        # posts = Post.objects.all().order_by('-created_at')[:10]
        context = {'user': user}
        return render(request, "help/detail.html", context=context)

class CreateHelpNotice(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        # posts = user.posts.all()
        context = {'user': user}
        return render(request, "help/edit.html", context=context)
    
    # def post(self, request, *args, **kwargs):
    #     user = request.user
    #     form = CreatePostForm(request.POST)

class EditHelpNotice(LoginRequiredMixin, View):
    login_url = '/user/login'

    def get(self, request, *args, **kwargs):
        user = request.user
        context = {'user': user}
        return render(request, 'profile/edit.html', context)

    # def post(self, request, *args, **kwargs):
    #     user = request.user
    #     form = CreatePostForm(request.POST)

    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.author = user
    #         post.status = 1
    #         post.save()
    #         return redirect(post)

    #     return render(request, 'profile.edit.html', {'form': form})

class DeleteHelpNotice(LoginRequiredMixin, View):
    def delete(self, request, *args, **kwargs):
        post = get_object_or_404(Post, slug=kwargs['slug'])
        context = {'post': post}
        return render(request, "blog/detail.html", context=context)
