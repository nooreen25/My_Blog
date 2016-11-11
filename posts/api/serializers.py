from rest_framework.serializers import (
          ModelSerializer,
          HyperlinkedIdentityField,
          SerializerMethodField,
          )
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
  url=HyperlinkedIdentityField(
      view_name='posts-api:post_detail',
      lookup_field='id',

    )
  user=SerializerMethodField()
  


    

  class Meta:
    model=Post
    fields=[
              'url',
              'user',
              'title',
              'content',
              'publish',
              
            ]

  def get_user(self,obj):
    return str(obj.user.username)


  



	


class PostDetailSerializer(ModelSerializer):
  url=HyperlinkedIdentityField(
      view_name='posts-api:post_detail',
      lookup_field='id',

    )
  user=SerializerMethodField()
  image=SerializerMethodField()

  
  
  class Meta:
    model=Post
    fields=[
              'user',
              'url',
              'id',
              'title',
              'content',
              'publish',
              'image',

            ]

  def get_user(self,obj):
    return str(obj.user.username)

  def get_image(self,obj):
    try:
      image=obj.image.url
    except:
      image=None
    return image
	


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



