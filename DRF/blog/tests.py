from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post , Category

class Test_Create_Post_User(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name="Django")
        testUser = User.objects.create_user(
            username="TestUser1" , password="12345678"
        )
        test_post = Post.objects.create(category_id="1", title="BlackHole" ,
            excerpt="BlackHole" , content="BlackHole" ,author_id=1
            ,status="published")

    def test_content(self):
        post = Post.objects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        content = f'{post.content}'
        title = f'{post.title}'
        status = f'{post.status}'
        self.assertEqual(author,'TestUser1')
        self.assertEqual(title,'BlackHole')
        self.assertEqual(content,'BlackHole')
        self.assertEqual(status,'published')
