from rest_framework.serializers import ModelSerializer
from posts.models import Post


class PostCreateSerializer(ModelSerializer):
	class Meta:
		model=Post
		fields=[
              'title',
              'content',
              'publish',
            ]



class PostListSerializer(ModelSerializer):
	class Meta:
		model=Post
		fields=[
		      'user',
              'title',
              'content',
              'publish',
            ]



class PostDetailSerializer(ModelSerializer):
	class Meta:
		model=Post
		fields=[
		      'id',
              'title',
              'content',
              'publish',
            ]


class PostUpdateSerializer(ModelSerializer):
	class Meta:
		model=Post
		fields=[
		      'id',
              'title',
              'content',
              'publish',
            ]


class PostDeleteSerializer(ModelSerializer):
	class Meta:
		model=Post
		fields=[
		      'id',
              'title',
              'content',
              'publish',
            ]
