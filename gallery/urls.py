from django.conf.urls import patterns, include, url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
                       url(r'^$', views.gallery, name='gallery'),
                       url(r'^album/(?P<id>\d+)/$', views.album, name='album'),
]
