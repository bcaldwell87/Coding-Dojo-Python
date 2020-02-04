from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^shows$', views.index),
    url(r'^shows/new$', views.newshow),
    url(r'^shows/create$', views.create),
    url(r'^shows/(?P<id>[0-9]+)$', views.viewshow),
    url(r'^shows/destroy/(?P<id>[0-9]+)$', views.destroy),
    url(r'^shows/(?P<id>[0-9]+)/edit$', views.edit),
    url(r'^shows/(?P<id>[0-9]+)/update$', views.update),
]