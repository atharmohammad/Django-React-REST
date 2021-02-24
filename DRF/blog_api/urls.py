from django.urls import path
from .views import PostList,PostListSearchView
from rest_framework import routers

app_name="blog_api"

router = routers.DefaultRouter()
router.register('post',PostList,basename='post')


urlpatterns = [
    path('search/',PostListSearchView.as_view(),name='search'),
]

urlpatterns += router.urls
