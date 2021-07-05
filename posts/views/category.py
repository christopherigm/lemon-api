from rest_framework.viewsets import ModelViewSet
from posts.models import Category
from posts.serializers import CategorySerializer


class CategoryViewSet ( ModelViewSet ):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    ordering = ['order']
    filterset_fields = {
        'id': ('exact',),
        'slug': ('exact',),
        'hashtag': ('exact',)
    }
    search_fields = [
        'title',
        'description'
        'slug',
        'hashtag'
    ]
