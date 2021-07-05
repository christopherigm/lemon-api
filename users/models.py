import uuid
from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from common.tools import set_media_url
from common.models import (
    CommonFields,
    Address,
    City
)

def picture(instance, filename):
    return set_media_url('profile', filename)

# Create your models here.

class UserAddress(Address):
    user = models.ForeignKey (
        User,
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )
    city = models.ForeignKey (
        City,
        related_name = 'user_city_address',
        null = True,
        blank = True,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.alias

    class Meta:
        verbose_name = 'User address'
        verbose_name_plural = 'User address'

    class JSONAPIMeta:
        resource_name = 'UserAddress'

class UserProfile(CommonFields):
    user = models.ForeignKey (
        User,
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )
    token = models.UUIDField (
        null = True,
        blank = True,
        default=uuid.uuid4
    )
    newsletter = models.BooleanField (
        default=False,
        blank=False,
        null=False
    )
    img_picture = ResizedImageField (
        null=True,
        blank=True,
        size=[512, 512],
        quality=90,
        upload_to=picture
    )
    promotions = models.BooleanField (
        default=False,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'User profile'
        verbose_name_plural = 'User profiles'

    class JSONAPIMeta:
        resource_name = 'UserProfile'
