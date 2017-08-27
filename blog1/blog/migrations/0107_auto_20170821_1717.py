# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 21:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0106_auto_20170821_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='fotos',
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Foto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 21, 21, 17, 53, 581538, tzinfo=utc)),
        ),
    ]
