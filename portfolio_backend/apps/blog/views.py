# -*- coding: utf-8 -*-

from rest_framework import viewsets

from portfolio_backend.apps.blog.models import Post
from portfolio_backend.apps.blog.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

