#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

setup(name='portfolio_backend',
      version='0.1',
      description='Backend service for my personal website',
      author='Swan Mougnoz',
      author_email='contact@swanmougnoz.net',
      packages=find_packages(),
      include_package_data=True,
      package_data={
          '': ['*.ini', '*.html', '*.js', '*.css', '*.jpg', '*.png']
      },
)


