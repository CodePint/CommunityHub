from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import View
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime, timedelta
from django.forms import modelform_factory



from .models import HelpNotice, User
from .forms import HelpNoticeForm, HelpNoticeForm

class HelpIndex(View):
    def get(self, request, type='', *args, **kwargs):
        if type:
            type = type.lower()
            notices = HelpNotice.objects.filter(type=type)[:10]
        else:
            type = 'all'
            notices = HelpNotice.objects.order_by('-created_at')[:10]
        context = {'type': type, 'notices': notices}
        return render(request, "help/index.html", context=context)

class HelpNoticeDetail(View):
    def get(self, request, type, slug, *args, **kwargs):
        user = request.user
        # help_filter = HelpNotice.objects.filter(type=type)
        notice = get_object_or_404(HelpNotice, slug=slug)
        context = {'user': user, 'notice': notice }
        return render(request, "help/detail.html", context=context)

class CreateHelpNotice(LoginRequiredMixin, View):
    login_url = '/user/login'

    def get(self, request, type, *args, **kwargs):
        user = request.user
        context = {'user': user, 'form': HelpNoticeForm(created=True)}
        return render(request, "help/create.html", context=context)
    
    def post(self, request, type, *args, **kwargs):
        user = request.user
        form = HelpNoticeForm(request.POST, created=True)

        if form.is_valid():
            notice = form.save(commit=False)
            notice.type = type
            notice.user = user
            notice.save()
            return redirect(notice)

        return render(request, 'help/create', {'form': form})

class EditHelpNotice(LoginRequiredMixin, View):
    login_url = '/user/login'

    def get(self, request, slug, *args, **kwargs):
        user = request.user
        notice = get_object_or_404(HelpNotice, slug=slug)
        form = HelpNoticeForm(initial=notice.form_fields())
        context = {'form': form, 'user': user, 'notice': notice}
        return render(request, 'help/edit.html', context)

    def post(self, request, slug, *args, **kwargs):
        user = request.user
        notice = get_object_or_404(HelpNotice, slug=slug)
        form = HelpNoticeForm(request.POST, instance=notice)

        if form.is_valid():
            notice = form.save(commit=False)
            notice.user = user
            notice.save()
            return redirect(notice)

        return render(request, 'help/edit.html', {'form': form})

class DeleteHelpNotice(LoginRequiredMixin, View):

    def get(self, request, slug, *args, **kwargs):
        notice = get_object_or_404(HelpNotice, slug=slug)
        context = {'notice': notice}
        return render(request, "help/delete.html", context)

    def post(self, request, slug, *args, **kwargs):
        notice = get_object_or_404(HelpNotice, slug=slug)
        message = "Help notice has been deleted - {}".format(notice.title)
        notice.delete()
        return redirect("helpme:index", type='')
