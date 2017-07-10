# -*- coding: utf-8 -*-

from rest_framework import viewsets

from portfolio_backend.apps.blog.models import Post, Comment
from portfolio_backend.apps.blog.serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['post_pk'])
