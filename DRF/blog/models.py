from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.

#Uplaoding file path Function
def upload_to(instance,filename):
    return 'posts/{filename}'.format(filename=filename)


class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Post(models.Model):

    class PostObjects(models.Manager): #custom manager
        #Now out model will first filter according to published post and then store
        #so we dont need to filter them in the views
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = ( #Choices Generated as select box insead of normal text field
        ('draft','Draft'),
        ('published','Published')
    )
    category = models.ForeignKey(Category,on_delete=models.PROTECT , default=1)
    title = models.CharField(max_length=256)
    image = models.ImageField(
    _("image"),upload_to=upload_to,default='posts/default.png',blank=True)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250,unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='blog_post')
    status = models.CharField(max_length=10,choices=options,default='published')
    objects = models.Manager() #default manager
    postobjects = PostObjects() #custom manager

    class Meta :
        ordering = ('-published',)

    def __str__(self):
        return self.title
