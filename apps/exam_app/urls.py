from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main$', views.main),
    url(r'^show/(?P<id>\d+)$',views.show),
    url(r'^addfriend/(?P<id>\d+)$',views.addfriend),
    url(r'^remove/(?P<id>\d+)$',views.remove),
]
