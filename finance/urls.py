from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	url(r'^$', views.login_page, name='login_page'),
	#url(r'^home/$', views.home_page, name='home_page'),
	url(r'^new/Money/$', views.new_Money, name='new_Money'),
	url(r'^canvas/$', views.canvas_test, name='canvas_test'),
	url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', views.signup, name='signup'),
]