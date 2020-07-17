"""
"""
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    body = models.TextField(null=True)

    slug = models.SlugField(max_length=255)

    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    total_likes = models.BigIntegerField(default=0)
    total_comments = models.BigIntegerField(default=0)

    deleted = models.BooleanField(default=False)

    class Meta:
        """
        """
        app_label = 'blog'


class PostLike(models.Model):
    """
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        """
        """
        app_label = 'blog'


class PostComment(models.Model):
    """
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.TextField()

    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    deleted = models.BooleanField(default=False)

    class Meta:
        """
        """
        app_label = 'blog'
