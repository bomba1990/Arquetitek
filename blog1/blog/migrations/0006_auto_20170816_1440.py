# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(default=1, upload_to='blog/imagenes'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=models.TextField(max_length=700),
        ),
    ]
