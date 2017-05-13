from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.login_page, name='login_page'),
	url(r'^home/$', views.home_page, name="home_page")
]