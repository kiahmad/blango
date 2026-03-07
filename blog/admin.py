from django.contrib import admin
from django.contrib.admin import ModelAdmin
from blog.models import Tag, Post, Comment, PostAdmin

# Register your models here.

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

    