# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 22:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0147_auto_20170824_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 24, 22, 35, 45, 406499, tzinfo=utc)),
        ),
    ]