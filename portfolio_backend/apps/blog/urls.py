from django.conf.urls import url, include
from rest_framework_nested import routers

from portfolio_backend.apps.blog import views
from portfolio_backend.apps.blog.views import PostCommentViewSet

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

posts_router = routers.NestedSimpleRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', PostCommentViewSet, base_name='post-comments')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(posts_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]