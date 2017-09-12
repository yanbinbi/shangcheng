from django.conf.urls import url
from django.contrib import admin
from user_manage import views

urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', views.register, name="register"),
    url(r'^email_register/$', views.email_register, name="email_register"),
    url(r'^phone_register/$', views.phone_register, name="phone_register"),
    url(r'^login/$', views.do_login, name="login"),
    url(r'^index/$', views.index, name="index"),
]
