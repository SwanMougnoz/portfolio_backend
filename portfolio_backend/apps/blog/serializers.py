from rest_framework import serializers

from portfolio_backend.apps.blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = []
