"""
"""
from django.contrib import admin

from .models import Post, PostComment, PostLike


class PostAdmin(admin.ModelAdmin):
    """
    """
    prepopulated_fields = {'slug': ('title',), }

admin.site.register(Post, PostAdmin)
admin.site.register(PostLike)
admin.site.register(PostComment)
