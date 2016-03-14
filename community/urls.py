from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
                    url(r'^$', views.committee, name= 'committee'),
                    url(r'^(?P<time>[2]\d{3}-[2]\d{3})/$', views.committee, name='previous_committee'),
                    url(r'^registration/$', views.registration, name='registr'),
                    url(r'^database/$', views.database, name='database'),
]
