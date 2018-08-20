# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-29 14:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
#import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0013_auto_20180324_0637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile_pic',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile_pic',
            name='user',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profile_pic', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
