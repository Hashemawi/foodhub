from django.conf.urls import url
from restaurants import views

urlpatterns = [
    
    url(r'^restaurant_list/$', views.restaurant_list, name="restaurant_list"),
    url(r'^detail/(?P<restaurant_id>\d+)/$', views.restaurant_detail, name="restaurant_detail"),

  
]