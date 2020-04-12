from django.urls import path, re_path

from . import views

app_name = 'helpme'
urlpatterns = [
    # match '' or capture param (wanted, offered) for viewing the index
    re_path(r'^(?P<type>|wanted|offered)/?$(?i)', views.HelpIndex.as_view(), name='index'),
    
    # capture type param (wanted, offered), and HelpNotice slug param for viewing notice detail
    re_path(r'^notice/(?P<type>wanted|offered)/(?P<slug>[-\w]+)/$(?i)', views.HelpNoticeDetail.as_view(), name='detail'),
    
    # capture type param (wanted, offered) for creating the notice
    re_path(r'^notice/(?P<type>|wanted|offered)/create$(?i)', views.CreateHelpNotice.as_view(), name='create'),

    # capture slug param for editing/deleting the notice
    re_path(r'^notice/(?P<slug>[-\w]+)/edit/$(?i)', views.EditHelpNotice.as_view(), name='edit'),
    re_path(r'^notice/(?P<slug>[-\w]+)/delete/$(?i)', views.DeleteHelpNotice.as_view(), name='delete'),
]
