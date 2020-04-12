from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import View


from .models import User, Profile
from .forms import ProfileEditForm


class IndexView(generic.ListView):
    template_name = 'users/index.html'
    queryset = User.objects.all()
    context_object_name = 'users'

class ProfileView(generic.DetailView):
    model = User
    template_name = 'profile/profile.html'

class ProfileEdit(View):
    login_url = '/user/login'

    def get(self, request, *args, **kwargs):
        user = request.user
        initial = user.profile.form_dict()
        form = ProfileEditForm(initial=initial)
        context = {'user': user, 'form': form}
        return render(request, 'profile/edit.html', context)

    def post(self, request, *args, **kwargs):
        user = request.user
        form = ProfileEditForm(request.POST or None, request.FILES, instance=user.profile)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect(profile)
        return render(request, 'profile/edit.html', {'form': form})




