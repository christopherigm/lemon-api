from django.db import models
from colorfield.fields import ColorField
from common.models import Picture

class Category(Picture):
    slug = models.SlugField (
        max_length = 64,
        null = True,
        blank = True
    )
    hashtag=models.ForeignKey (
        'posts.Hashtag',
        related_name='category_hashtag',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    icon=models.CharField (
        null=True,
        blank=True,
        max_length=32
    )
    order=models.PositiveIntegerField (
        null=True,
        blank=True,
        default=1
    )
    color=ColorField(
        null=True,
        blank=True,
        default='#42a5f5'
    )

    def __str__(self):
        return self.title

    class JSONAPIMeta:
        resource_name = 'Category'
