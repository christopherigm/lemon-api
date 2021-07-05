from rest_framework.viewsets import ModelViewSet
from posts.models import Hashtag
from posts.serializers import HashtagSerializer


class HashtagViewSet ( ModelViewSet ):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    ordering = ['order']
    filterset_fields = {
        'id': ('exact',),
        'hashtag': ('exact',)
    }
    search_fields = [
        'hashtag'
    ]
