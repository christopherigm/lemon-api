# Generated by Django 3.0.6 on 2021-07-04 18:14

import common.models.country
import common.models.state
import common.validators
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('version', models.PositiveIntegerField(default=1)),
                ('name', models.CharField(max_length=32, unique=True, validators=[common.validators.ModelValidators.name])),
                ('code', models.CharField(max_length=2, unique=True)),
                ('phone_code', models.CharField(max_length=2, unique=True)),
                ('img_flag', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=100, size=[128, 128], upload_to=common.models.country.picture)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Font',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('version', models.PositiveIntegerField(default=1)),
                ('name', models.CharField(max_length=32)),
                ('family', models.CharField(max_length=128)),
                ('css', models.CharField(max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('version', models.PositiveIntegerField(default=1)),
                ('name', models.CharField(max_length=32, unique=True, validators=[common.validators.ModelValidators.name])),
                ('code', models.CharField(max_length=4, unique=True)),
                ('img_flag', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=100, size=[128, 128], upload_to=common.models.state.picture)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('version', models.PositiveIntegerField(default=1)),
                ('name', models.CharField(max_length=32, unique=True, validators=[common.validators.ModelValidators.name])),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.State')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
