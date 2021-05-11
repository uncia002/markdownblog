# coding: utf-8

from rest_framework import routers
from .views import CategoryViewSet, BlogViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'blogs', BlogViewSet)
router.register(r'comments', CommentViewSet)
