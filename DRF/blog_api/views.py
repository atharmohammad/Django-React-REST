from .serializers import PostSerializer,PostListSerializer
from blog.models import Post
from django.contrib.auth.models import User
from rest_framework import generics,viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import filters
from rest_framework.permissions import (SAFE_METHODS,BasePermission,IsAuthenticated,AllowAny,
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

class PostList(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self,request):
        self.queryset = Post.objects.all()
        serializer_class = PostListSerializer(self.queryset,many=True)
        return Response(serializer_class.data)

    def create(self,request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
        
    def retrieve(self,request,pk=None):
        self.queryset = Post.objects.filter(author=request.user)
        post = get_object_or_404(self.queryset,pk=pk)
        serializer_class = PostSerializer(post)
        return Response(serializer_class.data)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()



class PostListSearchView(generics.ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']

# class PostDetail(generics.RetrieveUpdateDestroyAPIView,PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
