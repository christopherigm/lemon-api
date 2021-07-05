from rest_framework_json_api.serializers import HyperlinkedModelSerializer
from posts.models import Hashtag

# Create your serializers here.

class HashtagSerializer(HyperlinkedModelSerializer):
    
    class Meta:
        model = Hashtag
        fields = '__all__'
