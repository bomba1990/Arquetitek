# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 02:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0162_auto_20170825_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, upload_to='blog/fotos/portafolio')),
            ],
        ),
        migrations.RemoveField(
            model_name='foto',
            name='portafolio',
        ),
        migrations.AlterField(
            model_name='portafolio',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='blog/fotos/portafolio'),
        ),
        migrations.AlterField(
            model_name='portafolio',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 26, 2, 49, 15, 479163, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 26, 2, 49, 15, 478092, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='fotos',
            name='portafolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Portafolio'),
        ),
    ]
