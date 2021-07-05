from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.serializers import PostSerializer


class PostViewSet ( ModelViewSet ):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    ordering = ['id']
    filterset_fields = {
        'id': ('exact',),
        'category': ('exact',),
        'author': ('exact',),
        'slug': ('exact',),
        'hashtags': ('exact',)
    }
    search_fields = [
        'title',
        'description',
        'category',
        'slug',
        'hashtags'
    ]
