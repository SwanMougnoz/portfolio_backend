from rest_framework import serializers

from portfolio_backend.apps.blog.models import Post, Tag, Comment


class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, slug_field='label', queryset=Tag.objects.all())

    class Meta:
        model = Post
        exclude = []


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = []
