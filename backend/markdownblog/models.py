from django.db import models
from markdownx.models import MarkdownxField

class Category(models.Model):
    name = models.CharField('カテゴリ名',max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='カテゴリ')
    title = models.CharField(blank=False, null=False, max_length=150)
    thumbnail = models.ImageField('サムネイル', blank=True, null=True)
    text = MarkdownxField('本文', help_text='Markdown形式で書いてください。')
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(blank=False,null=False)
    blog = models.ForeignKey(Category,on_delete=models.CASCADE, verbose_name="")
    def __str__(self):
        return self.text
