from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard/$', views.dashboard),
    url(r'^jobs/new$', views.newjob),
    url(r'^logout$', views.logout),
    url(r'^job/create$', views.createjob),
    url(r'^jobs/(?P<id>[0-9]+)$', views.show_job),
    url(r'^jobs/(?P<id>[0-9]+)/add$', views.addjob),
    url(r'^jobs/(?P<id>[0-9]+)/edit$', views.edit),
    url(r'^job/(?P<id>[0-9]+)/update$', views.update),
]