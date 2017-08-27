# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 21:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0050_auto_20170818_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foto',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='foto',
            name='titulo',
        ),
        migrations.AddField(
            model_name='foto',
            name='Post',
            field=models.ManyToManyField(to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 18, 21, 29, 24, 470779, tzinfo=utc)),
        ),
    ]
