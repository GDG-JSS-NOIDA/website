# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-31 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20170831_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, max_length=40, null=True),
        ),
    ]
