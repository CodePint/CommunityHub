from django.urls import path, re_path

from . import views

app_name = 'helpme'
urlpatterns = [
    # match '' or capture param of (wanted, offered)
    re_path(r'^(?P<type>|wanted|offered)/?$', views.HelpIndex.as_view(), name='index'),

    # allow url part (wanted, offered), and match slug param
    re_path(r'^(wanted|offered)/(P<slug>[\w-]+)/$', views.HelpDetail.as_view(), name='detail'),

    # match '/create' and capture param of (wanted, offered)
    re_path(r'^create/(P<type>wanted|offered)/$', views.CreateHelpNotice.as_view(), name='create'),

    # match '/edit', '/delete' part, allow url part (wanted, offered), and capture slug param
    re_path(r'^edit/(wanted|offered)/(?P<slug>[\w-]+)$', views.EditHelpNotice.as_view(), name='edit'),
    re_path(r'^delete/(wanted|offered)/(?P<slug>[\w-]+)$', views.DeleteHelpNotice.as_view(), name='delete'),
]
