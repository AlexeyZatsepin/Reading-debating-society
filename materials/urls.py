from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
                       url(r'^$', views.materials, name='materials'),
                       url(r'^material/(?P<id>\d+)/$', views.material , name='material'),
                       url(r'^events/$', views.events , name='events'),
                       url(r'^event/(?P<id>\d+)/$', views.event , name='event'),
]