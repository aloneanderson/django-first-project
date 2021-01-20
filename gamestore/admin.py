from django.contrib import admin
from .models import Article, Comment, Like, DisLike, Author, Book


class ArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(DisLike)
