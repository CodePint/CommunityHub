from django.urls import path, re_path

from . import views

app_name = 'helpme'
urlpatterns = [
    # match '' or capture type param of tuple (wanted, offered)
    re_path(r'^(?P<type>|wanted|offered)/?$', views.HelpIndex.as_view(), name='index'),
    re_path(r'^(?P<slug>[\w-]+)/(wanted|offered)/$', views.HelpDetail.as_view(), name='detail'),
    re_path(r'^create/(P<type>wanted|offered)/$', views.CreateHelpNotice.as_view(), name='create'),
    re_path(r'^edit/(wanted|offered)/(?P<slug>[\w-]+)$', views.EditHelpNotice.as_view(), name='edit'),
    re_path(r'^delete/(wanted|offered)/(?P<slug>[\w-]+)$', views.DeleteHelpNotice.as_view(), name='delete'),
]
