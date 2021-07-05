from rest_framework_json_api.serializers import HyperlinkedModelSerializer
from rest_framework_json_api.relations import ResourceRelatedField
from posts.models import (
    Category,
    Hashtag
)

# Create your serializers here.

class CategorySerializer(HyperlinkedModelSerializer):
    hashtag = ResourceRelatedField (
        queryset = Hashtag.objects
    )

    included_serializers = {
        'hashtag': 'posts.serializers.HashtagSerializer'
    }
    
    class Meta:
        model = Category
        fields = '__all__'
