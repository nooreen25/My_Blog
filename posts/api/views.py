from django.db.models import Q

from .pagination import PostLimitOffsetPagination,PostPageNumberPagination

#from rest_framework.filters import(
#    SearchFilter,
#    OrderingFilter,

#	)

from rest_framework.generics import (
	      ListAPIView,
	      RetrieveAPIView,
	      RetrieveUpdateAPIView,
	      DestroyAPIView,
	      CreateAPIView,
	      )

from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,


	)
from posts.models import Post
from .serializers import PostDetailSerializer,PostListSerializer,PostDeleteSerializer,PostUpdateSerializer,PostCreateSerializer
from .permissions import IsOwnerOrReadOnly

class PostCreateAPIView(CreateAPIView):
	queryset=Post.objects.all()
	serializer_class=PostCreateSerializer
	permission_classes=[IsAuthenticated]

	def perform_create(self,serializer):
		serializer.save(user=self.request.user)
	
    


class PostDetailAPIView(RetrieveAPIView):
	queryset=Post.objects.all()
	serializer_class=PostDetailSerializer
	lookup_field='id'
    

class PostUpdateAPIView(RetrieveUpdateAPIView):
	queryset=Post.objects.all()
	serializer_class=PostUpdateSerializer
	lookup_field='id'
	permission_classes=[IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

	def perform_update(self,serializer):
		serializer.save(user=self.request.user)
		
	
    

class PostDeleteAPIView(DestroyAPIView):
	queryset=Post.objects.all()
	serializer_class=PostDeleteSerializer
	lookup_field='id'
	permission_classes=[IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    
 
class PostListAPIView(ListAPIView):
    queryset=Post.objects.all() 
    serializer_class=PostListSerializer
    pagination_class=PostPageNumberPagination
    #filter_backends=[SearchFilter]
    #search_fields=['title','content','user__first_name']

    #def get_queryset(self,*args,**kwargs):
    	#queryset_list=Post.objects.all()
    	#query=self.request.Get.get("q")


    	#if query:
    	#	queryset_list=queryset_list.filter(
    	#		Q(title_icontains=query)|
    	#		Q(content_icontains=query)|
    	#		Q(user_first_name_icontains=query)|
    	#		Q(user_last_name_icontains=query)
    	#		).distinct()
    	#return queryset_list




    		
                    
                    
                    
                    
                    
    		
    	






    			


