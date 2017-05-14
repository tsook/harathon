from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	url(r'^$', auth_views.login, name='login'),
	url(r'^home/$', views.home_page, name='home_page'),
	url(r'^new/Money/$', views.new_Money, name='new_Money'),
	url(r'^accounts/profile/graph_view/$', views.graph_view, name='graph_view'),
	#url(r'^login/$', auth_views.login, {'template_name': 'finance/login_page.html'}, name='login'),
	url(r'^accounts/profile/$', views.home_page, name='home_page'),
	url(r'^accounts/profile/delete/', views.delete, name="delete"),
	url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^get_list/$', views.get_list, name='get_list')
]