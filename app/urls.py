from django.conf.urls import url
from . import views

urlpatterns = [
                       url(r'^$', views.index, name='welcome'),
                       url(r'^search/$', views.search , name='search'),
                       url(r'^debating/$', views.debating , name='debating'),
                       url(r'^sponsors/$', views.sponsors , name='sponsors'),
                       url(r'^contact/$', views.contact , name='contact'),
]
