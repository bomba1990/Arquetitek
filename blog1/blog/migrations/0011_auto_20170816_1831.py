# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170816_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='imagen',
            field=models.ImageField(upload_to='blog/fotos/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(upload_to='blog/fotos/'),
        ),
    ]
