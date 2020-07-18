"""
"""
from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    class Meta:
        model = Post
        fields = ('title', 'body', 'slug', 'added_at',
                  'updated_at', 'total_likes', 'total_comments')