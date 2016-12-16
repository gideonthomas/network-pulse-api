from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout', views.force_logout, name='logout'),
    url(r'^oauth2callback', views.callback, name='oauthcallback'),
    url(r'^nonce', views.nonce, name="get a new nonce value"),
]
