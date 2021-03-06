# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 16:16
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20171006_1210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='create',
            new_name='created_by',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='description',
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(upload_to=blog.models.upload_fotos),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='video',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
