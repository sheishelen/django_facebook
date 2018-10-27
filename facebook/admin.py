from django.contrib import admin

# Register your models here.

from facebook.models import Article, Page
admin.site.register(Article)
admin.site.register(Page)

from facebook.models import Comment, Page
admin.site.register(Comment)
