from django.db import models
from tinymce.models import HTMLField
from common.models import CommonFields
from common.tools import set_media_url
from django_resized import ResizedImageField

def picture(instance, filename):
  return set_media_url( 'CommonPicture', filename)

class Picture(CommonFields):
    title = models.CharField (
        max_length = 64,
        null = True,
        blank = True
    )
    description = HTMLField (
        null=True,
        blank=True
    )
    order = models.PositiveIntegerField (
        verbose_name="índice de ordenamiento",
        null=True,
        blank=True,
        default=0,
        help_text="Índice númerico de ordenamiento de este registro"
    )
    href = models.URLField (
        null = True,
        blank = True
    )
    # https://pypi.org/project/django-resized/
    img_picture = ResizedImageField (
        null=True,
        blank=True,
        size=[1280, 720],
        quality=90,
        upload_to=picture
    )

    class Meta:
        abstract = True
