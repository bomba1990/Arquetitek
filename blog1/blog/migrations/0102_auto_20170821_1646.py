# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 20:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0101_auto_20170821_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 21, 20, 46, 32, 57160, tzinfo=utc)),
        ),
    ]
