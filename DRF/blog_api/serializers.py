from rest_framework import serializers
from blog.models import Post

#so serializer used to convert our models data in json format and the fields we specify
#here will appear on /api url as we are using it in its view
class PostSerializer(serializers.ModelSerializer):
    class Meta :
        model = Post
        fields = ('id','title','author','excerpt','content','status')


class PostListSerializer(serializers.ModelSerializer):
    class Meta :
        model = Post
        fields = ('id','title','author','status')
