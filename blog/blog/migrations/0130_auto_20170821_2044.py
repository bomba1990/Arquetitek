# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 00:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0129_auto_20170821_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foto',
            name='foto',
        ),
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 22, 0, 44, 32, 401334, tzinfo=utc)),
        ),
    ]