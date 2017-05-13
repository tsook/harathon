from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.login_page, name='login_page'),
	url(r'^canvas/$', views.canvas_test, name='canvas_test')
]