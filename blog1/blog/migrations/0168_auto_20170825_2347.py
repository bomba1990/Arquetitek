# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 03:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0167_auto_20170825_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portafolio',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 26, 3, 47, 46, 434132, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 26, 3, 47, 46, 433193, tzinfo=utc)),
        ),
    ]
