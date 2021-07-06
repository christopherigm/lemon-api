from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from common.models import CommonFields
from common.tools import set_media_url
from django_resized import ResizedImageField

def picture(instance, filename):
    return set_media_url('Posts', filename)

class Post(CommonFields):
    title = models.CharField (
        max_length = 64,
        null=False,
        blank=False,
        unique=True
    )
    slug = models.SlugField (
        max_length = 64,
        null=False,
        blank=False,
        unique=True
    )
    category=models.ForeignKey (
        'posts.Category',
        related_name='post_category',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey (
        User,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    featured=models.BooleanField (
        blank=False,
        default=False
    )
    video=models.URLField(
        null=True,
        blank=True
    )
    description = HTMLField(
        null=True,
        blank=True
    )
    img_picture = ResizedImageField (
        null=True,
        blank=True,
        size=[1920, 1080],
        quality=90,
        upload_to=picture
    )
    hashtags=models.ManyToManyField (
        'posts.Hashtag',
        related_name='post_hashtags',
        blank=True
    )
    reference=models.URLField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class JSONAPIMeta:
        resource_name="Post"
