# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 19:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_auto_20170818_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='imagen',
            field=models.ImageField(upload_to='blog/fotos/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 18, 19, 44, 44, 315697, tzinfo=utc)),
        ),
    ]
