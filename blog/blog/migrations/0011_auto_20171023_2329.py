# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-24 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20171023_2318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'ordering': ['-completed']},
        ),
        migrations.AddField(
            model_name='portfolio',
            name='photos_col_size',
            field=models.IntegerField(default=3),
        ),
    ]
