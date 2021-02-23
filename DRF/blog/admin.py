from django.contrib import admin
from .models import Post,Category
# Register your models here.

@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','author','title','status','slug')
    prepopulated_fields = {'slug':('title',),}

admin.site.register(Category)
