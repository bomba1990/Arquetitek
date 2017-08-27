# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 14:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0066_auto_20170821_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foto',
            name='post',
        ),
        migrations.RemoveField(
            model_name='foto',
            name='titulo',
        ),
        migrations.AlterField(
            model_name='foto',
            name='imagen',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 21, 14, 40, 40, 354616, tzinfo=utc)),
        ),
    ]
