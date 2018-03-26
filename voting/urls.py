from django.conf.urls import url

from voting import views

urlpatterns = [

    url(r'^/(?P<vote_id>\d+)/', views.voter, name='voters'),
]
