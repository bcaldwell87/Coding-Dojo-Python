from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^books$', views.books),
    url(r'^books/create$', views.create_book),
    url(r'^books/(?P<id>[0-9]+)$', views.show_book),
    url(r'^books/(?P<book_id>[0-9]+)/addfavorite$', views.addfavorite),
    url(r'^books/(?P<book_id>[0-9]+)/update$', views.update),
    url(r'^books/(?P<id>[0-9]+)/delete_book$', views.delete_book),
    url(r'^books/(?P<id>[0-9]+)/unfavorite$', views.unfavorite),
]