from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase,APIClient
from blog.models import Post,Category
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.

class Test_Post_Api(APITestCase):
    def test_get_post(self):
        url =  reverse("blog_api:listcreate")
        response = self.client.get(url,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_post_Post(self):
        client = APIClient()
        self.test_Category = Category.objects.create(name="Django")
        self.user = User.objects.create_superuser(
            username="testUser1" , password="12345678"
        )
        self.client.login(username=self.user.username,password="12345678")
        data={
             "title":"new","author":1 , "excerpt":"new"
            ,"content":"new","status":"published"
        }
        url = reverse("blog_api:listcreate")
        response = self.client.post(url,data,format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_update_post(self):
        client = APIClient()
        self.test_category = Category.objects.create(name="django")
        self.test_user1 = User.objects.create_user(username="test_user1",password="12345678")
        self.test_user2 = User.objects.create_user(username="test_user2",password="12345678")
        test_post = Post.objects.create(category_id=1, title="BlackHole" ,
            excerpt="BlackHole" , content="BlackHole" ,author_id=1
            ,status="published")

        client.login(username=self.test_user1.username,password="12345678")
        url = reverse(("blog_api:detailcreate"),kwargs={'pk':1})
        response = self.client.put(
            url,{
            "title": "Space",
            "author": 1,
            "excerpt": "Space is black",
            "content": "Space is very large",
            "status": "published"
            },format='json'
        )
        print(response.data)
