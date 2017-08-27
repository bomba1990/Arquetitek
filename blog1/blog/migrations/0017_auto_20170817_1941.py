# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 23:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20170817_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='imagen',
            field=models.ImageField(upload_to='', verbose_name='blog/fotos/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 17, 23, 41, 25, 541224, tzinfo=utc)),
        ),
    ]
