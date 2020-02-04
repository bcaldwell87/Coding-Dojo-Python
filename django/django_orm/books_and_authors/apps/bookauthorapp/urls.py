from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^viewbook/(?P<id>[0-9]+)$', views.book),
    url(r'^addbook$', views.index),
    url(r'^authors$', views.authors),
    url(r'^viewauthor/(?P<id>[0-9]+)$', views.author),
    url(r'^addauthor$', views.authors),
]
