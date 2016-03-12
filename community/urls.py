from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
                    url(r'^$', views.committee, name= 'committee'),
                    url(r'^registration/$', views.registration, name='registr'),
]
