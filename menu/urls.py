from django.conf.urls import url
from . import views
from .views import CategoryListView
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', CategoryListView.as_view(), name='Revelmenu'),
    url(r'^menu/cnew/$', views.cat_new, name='cat_new'),
    url(r'^menu/pnew/$', views.prod_new, name='prod_new'),
    url(r'^menu/(?P<pk>\d+)/edit/$', views.cat_edit, name='cat_edit'),
    url(r'^menu/p(?P<pk>\d+)/edit/$', views.prod_edit, name='prod_edit'),
    url(r'^login/$', login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
]


