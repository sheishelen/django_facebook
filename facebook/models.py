from django.db import models

# Create your models here.

class Article (models.Model):
    author = models.CharField(max_length=10)
    title = models.CharField(max_length=120)
    text = models.TextField(default='')
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment (models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=10)
    text = models.TextField(default='')
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author


class Page (models.Model) :
    admin = models.CharField(max_length=20)
    page_name = models.CharField(max_length=80)
    text = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.page_name
