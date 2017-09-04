# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 19:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0089_auto_20170821_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='titulo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 21, 19, 35, 18, 253857, tzinfo=utc)),
        ),
    ]