# Generated by Django 3.0.6 on 2021-07-05 07:32

from django.db import migrations
import django_resized.forms
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='img_picture',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=90, size=[512, 512], upload_to=users.models.picture),
        ),
    ]