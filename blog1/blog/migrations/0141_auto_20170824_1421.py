# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 18:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0140_auto_20170823_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 24, 18, 21, 8, 368003, tzinfo=utc)),
        ),
    ]
