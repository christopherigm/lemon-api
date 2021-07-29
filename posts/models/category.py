from django.db import models
from colorfield.fields import ColorField
from common.models import Picture

class Category(Picture):
    slug = models.SlugField (
        max_length = 64,
        null=False,
        blank=True,
        unique=True
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
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self.title, Category)
        super().save(*args, **kwargs)

    class JSONAPIMeta:
        resource_name = 'Category'
