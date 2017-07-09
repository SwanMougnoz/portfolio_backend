# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    body = models.TextField()


class Comment(models.Model):
    author = models.CharField(max_length=64, null=True, blank=True)
    body = models.TextField()
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments')


class Tag(models.Model):
    label = models.CharField(max_length=32, null=False, blank=False)
    post = models.ForeignKey(to=Post, on_delete=models.PROTECT, related_name='tags')
