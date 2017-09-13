from django.conf.urls import url
from django.contrib import admin
from product_manage import views

urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    url(r'^index/$', views.index, name="index"),
]
