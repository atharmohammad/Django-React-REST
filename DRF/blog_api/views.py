from .serializers import PostSerializer,PostListSerializer
from blog.models import Post
from django.contrib.auth.models import User
from rest_framework import generics,viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework.permissions import (SAFE_METHODS,BasePermission,IsAuthenticated,
                IsAdminUser,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly)
# Create your views here.

class PostUserWritePermission(BasePermission):
    message = "Editting of Posts is authorised to User only"
    def has_object_permission(self,request,view,obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user

# Ok So here we created a customised permission using BasePermission so what we did is that
# if a user access a post which he had not created than it can only get it means read it only cannot
# Update it whereas if the post is created by him than he can update it also
# class PostUserPermission(BasePermission):
#     message = "Editting of Posts is authorised to User only"
#     def has_object_permission(self,request,view,obj):
#         if request.method in SAFE_METHODS:
#             return True
#
#         auth = User.objects.filter(request.user == username)
#         return auth

class PostList(viewsets.ViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Post.objects.all()


    def list(self,request):
        # self.queryset = Post.objects.filter(author=request.user)
        serializer_class = PostListSerializer(self.queryset,many=True)
        return Response(serializer_class.data)


    def retrieve(self,request,pk=None):
        # self.queryset = Post.objects.filter(author=request.user)
        post = get_object_or_404(self.queryset,slug=pk)
        serializer_class = PostSerializer(post)
        return Response(serializer_class.data)

class PostListSearchView(generics.ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']

# class PostDetail(generics.RetrieveUpdateDestroyAPIView,PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
