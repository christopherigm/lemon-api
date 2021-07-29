from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from common.models import CommonFields
from common.tools import set_media_url, get_unique_slug
from django_resized import ResizedImageField

def picture(instance, filename):
    return set_media_url('Posts', filename)

class Post(CommonFields):
    title = models.CharField (
        max_length = 128,
        null=False,
        blank=False,
        unique=True
    )
    slug = models.SlugField (
        max_length = 64,
        null=False,
        blank=True,
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
    og_title = models.CharField (
        max_length = 128,
        null=True,
        blank=True
    )
    og_description = models.CharField (
        max_length = 128,
        null=True,
        blank=True
    )
    img_og_picture = ResizedImageField (
        null=True,
        blank=True,
        size=[512, 512],
        quality=90,
        upload_to=picture
    )
    reference=models.URLField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self.title, Post)
        if not self.og_description:
            self.og_description = self.description
        if not self.og_title:
            self.og_title = self.title
        if not self.img_og_picture:
            self.img_og_picture = self.img_picture
        super().save(*args, **kwargs)

    class JSONAPIMeta:
        resource_name="Post"
