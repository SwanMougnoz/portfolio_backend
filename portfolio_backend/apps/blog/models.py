# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Tag(models.Model):
    label = models.CharField(max_length=32, null=False, blank=False, unique=True)

    def __unicode__(self):
        return self.label


class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    body = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(to=Tag, related_name='tagged_posts')

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=64, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments')
