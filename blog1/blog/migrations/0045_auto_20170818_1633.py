# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 20:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0044_auto_20170818_1627'),
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
            name='imagen',
            field=models.ImageField(upload_to='blog/fotos/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 18, 20, 33, 17, 181492, tzinfo=utc)),
        ),
    ]
