from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
                       url(r'^$', views.materials, name='materials'),
                       url(r'^events/$', views.events , name='events'),
                       url(r'^workshops/$', views.workshops , name='workshops'),
                       url(r'^download/(?P<file_name>.+)$', views.download , name='download'),
                       #url(r'^event/(?P<id>\d+)/$', views.event , name='event'),

]