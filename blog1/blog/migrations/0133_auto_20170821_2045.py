# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 00:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0132_auto_20170821_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 22, 0, 45, 33, 353419, tzinfo=utc)),
        ),
    ]
