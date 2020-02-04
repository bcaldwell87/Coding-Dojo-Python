from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^wishes/$', views.dashboard),
    url(r'^wish/new$', views.newwish),
    url(r'^logout$', views.logout),
    url(r'^wish/create$', views.createwish),
    url(r'^wish/(?P<id>[0-9]+)/delete$', views.destroywish),
    url(r'^wishes/edit/(?P<id>[0-9]+)$', views.edit),
    url(r'^wishes/update/(?P<id>[0-9]+)$', views.update),
    url(r'^wish/(?P<id>[0-9]+)/remove$', views.wishgranted),
]