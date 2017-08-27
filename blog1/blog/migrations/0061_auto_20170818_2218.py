# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 02:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0060_auto_20170818_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='foto',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 19, 2, 17, 58, 87608, tzinfo=utc)),
        ),
    ]
