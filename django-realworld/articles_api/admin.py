from django.contrib import admin
from articles_api.models import Article, Comment, Tag
# Register your models here.

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Tag)