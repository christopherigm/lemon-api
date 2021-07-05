from rest_framework_json_api.serializers import HyperlinkedModelSerializer
from rest_framework_json_api.relations import ResourceRelatedField
from posts.models import (
    Post,
    Category,
    Hashtag
)
from django.contrib.auth.models import User

# Create your serializers here.

class PostSerializer(HyperlinkedModelSerializer):
    category = ResourceRelatedField (
        queryset = Category.objects
    )
    hashtags = ResourceRelatedField (
        queryset = Hashtag.objects,
        many=True
    )
    author = ResourceRelatedField (
        queryset = User.objects
    )

    included_serializers = {
        'category': 'posts.serializers.CategorySerializer',
        'hashtags': 'posts.serializers.HashtagSerializer',
        'author': 'users.serializers.UserSerializer'
    }

    class Meta:
        model = Post
        fields = '__all__'
