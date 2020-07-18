"""src.api URL Configuration
"""
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('articles/', views.ArticleList.as_view()),
    path('articles/<slug:slug>/', views.ArticleDetails.as_view()),

    path('articles/<slug:slug>/comments/', views.ArticleCommentList.as_view()),
    #path('articles/<slug:slug>/comments/<int:pk>', views.ArticleCommentDetails.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)