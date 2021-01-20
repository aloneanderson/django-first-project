from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=120)


class Book(models.Model):
    name = models.CharField(max_length=120)
    year_of_public = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField(max_length=50000, null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Article created by {self.user}'


class Comment(models.Model):
    text = models.CharField(max_length=500)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comment = models.ForeignKey('gamestore.Comment', null=True, blank=True, on_delete=models.DO_NOTHING,
                                related_name='comments')

    def __str__(self):
        return f'Comment: {self.text} commented by user: {self.user}'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    comment = models.ForeignKey(Comment, on_delete=models.DO_NOTHING)


class DisLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    comment = models.ForeignKey(Comment, on_delete=models.DO_NOTHING)
