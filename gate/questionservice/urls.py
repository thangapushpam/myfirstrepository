from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^view_adminpage/$', views.view_adminpage, name='view_adminpage'),
    url(r'^view_studentpage/$', views.view_studentpage, name='view_studentpage'),
    url(r'^get_value/$', views.get_value, name='get_value'),
    url(r'^add/$', views.add, name='add'),
    url(r'^view_questionpage/$', views.view_questionpage, name='view_questionpage'),
    url(r'^validate/(?P<id>[0-9]+)/$', views.validate, name='validate'),
    url(r'^logout_view/$', views.logout_view, name='logout_view'),
    url(r'^logout/$', views.logout, name='logout'),
    #url(r'^create/$', views.create, name='create'),
    ]