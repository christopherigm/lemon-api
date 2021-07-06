from django.db import models
from common.models import CommonFields

class Hashtag(CommonFields):
    hashtag = models.SlugField (
        max_length = 32,
        null = True,
        blank = True,
        unique=True
    )
    order=models.PositiveIntegerField (
        null=True,
        blank=True,
        default=1
    )

    def __str__(self):
        return self.hashtag

    class JSONAPIMeta:
        resource_name = 'Hashtag'
