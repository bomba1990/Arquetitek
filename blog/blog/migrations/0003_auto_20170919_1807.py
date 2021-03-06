# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 22:07
from __future__ import unicode_literals

import blog.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170917_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='portafolio',
            name='publicado',
        ),
        migrations.AddField(
            model_name='foto',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 9, 19, 22, 7, 34, 75547, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foto',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='photos',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 9, 19, 22, 7, 38, 155456, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photos',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='portafolio',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 9, 19, 22, 7, 41, 675204, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portafolio',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 9, 19, 22, 7, 44, 943664, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='foto',
            name='foto',
            field=models.ImageField(blank=True, upload_to=blog.models.upload_fotos),
        ),
        migrations.AlterField(
            model_name='photos',
            name='foto',
            field=models.ImageField(blank=True, upload_to=blog.models.upload_fotos),
        ),
        migrations.AlterField(
            model_name='portafolio',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='portafolio',
            name='completed',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='portafolio',
            name='imagen',
            field=models.ImageField(blank=True, upload_to=blog.models.upload_fotos),
        ),
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, upload_to=blog.models.upload_fotos),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
