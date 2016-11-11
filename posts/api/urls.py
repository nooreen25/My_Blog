from django.conf.urls import url

from views import (
	PostCreateAPIView,
	PostListAPIView,
	PostDetailAPIView,
	PostUpdateAPIView,
	PostDeleteAPIView,
	)


urlpatterns = [
    url(r'^$',PostListAPIView.as_view(), name='post_list'),
    url(r'^create/$', PostCreateAPIView.as_view(), name='post_create'),
    #url(r'^(?P<id>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<id>[0-9]+)/$', PostDetailAPIView.as_view(), name='post_detail'),
    url(r'^(?P<id>[0-9]+)/edit/$', PostUpdateAPIView.as_view(), name='post_update'),
    url(r'^(?P<id>[0-9]+)/delete/$', PostDeleteAPIView.as_view(), name='post_delete'),
    

]