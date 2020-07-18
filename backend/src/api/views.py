"""
"""
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializer
from blog.models import Post, PostComment


class ArticleList(APIView):
    """
    """
    def get(self, request, format=None):
        """
        :param request:
        :param format:
        :return:
        """
        posts = Post.objects.filter(deleted=False)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class ArticleDetails(APIView):
    """
    """
    def get_post(self, slug):
        """
        :param slug:
        :return:
        """
        try:
            return Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        """
        :param request:
        :param slug:
        :param format:
        :return:
        """
        snippet = self.get_post(slug)
        serializer = PostSerializer(snippet)
        return Response(serializer.data)


class ArticleCommentList(APIView):
    """
    """
    def get(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        post_slug = kwargs['slug']
        #posts = PostComment.objects.filter(deleted=False)
        #serializer = PostCommentSerializer(posts, many=True)
        #return Response(serializer.data)
        pass