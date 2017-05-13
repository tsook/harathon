from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.login_page, name='login_page'),
	url(r'^home/$', views.home_page, name="home_page"),
	url(r'^new/Money/$', views.new_Money, name='new_Money'),
	url(r'^canvas/$', views.canvas_test, name='canvas_test')
]