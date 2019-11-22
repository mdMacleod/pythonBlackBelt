from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    url(r'^register$', views.register),
    url(r'^dashboard$', views.dashboard),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^logout$', views.logout),
    url(r'^user/(?P<id>\d+)$', views.user),
    url(r'^newquote$', views.newquote),
    url(r'^addfavorite/(?P<id>\d+)$', views.addfavorite),
    url(r'^removefavorite/(?P<id>\d+)$', views.removefavorite),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^editredirect/(?P<id>\d+)$', views.editredirect),
]