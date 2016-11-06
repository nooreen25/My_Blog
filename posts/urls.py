from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^create/$', views.post_create, name='post_create'),
    url(r'^(?P<id>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<id>[0-9]+)/edit/$', views.post_update, name='post_update'),
    url(r'^(?P<id>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
    

]