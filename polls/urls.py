from django.conf.urls import url

from polls import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)$', views.detail, name='details'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^display/(?P<question_id>[0-9]+)/', views.display, name='graph'),


]