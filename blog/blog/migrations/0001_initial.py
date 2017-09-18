# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 03:43
from __future__ import unicode_literals

import ckeditor_uploader.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, upload_to='blog/fotos/')),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, upload_to='blog/fotos/portafolio')),
            ],
        ),
        migrations.CreateModel(
            name='Portafolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('contenido', ckeditor_uploader.fields.RichTextUploadingField()),
                ('imagen', models.ImageField(blank=True, upload_to='blog/fotos/portafolio')),
                ('video', models.CharField(blank=True, max_length=200)),
                ('slug', models.SlugField(editable=False)),
                ('presentar', models.BooleanField(default=True)),
                ('create', models.CharField(max_length=200)),
                ('completed', models.DateField(default=datetime.datetime(2017, 9, 18, 3, 43, 4, 953369, tzinfo=utc))),
                ('skills', models.CharField(max_length=200)),
                ('client', models.CharField(max_length=200)),
                ('publicado', models.DateField(default=datetime.datetime(2017, 9, 18, 3, 43, 4, 953438, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('contenido', ckeditor_uploader.fields.RichTextUploadingField()),
                ('imagen', models.ImageField(blank=True, upload_to='blog/fotos/')),
                ('video', models.CharField(blank=True, max_length=200)),
                ('slug', models.SlugField(editable=False)),
                ('presentar', models.BooleanField(default=True)),
                ('publicado', models.DateField(default=datetime.datetime(2017, 9, 18, 3, 43, 4, 952508, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.UserProfile'),
        ),
        migrations.AddField(
            model_name='portafolio',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.UserProfile'),
        ),
        migrations.AddField(
            model_name='photos',
            name='portafolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Portafolio'),
        ),
        migrations.AddField(
            model_name='foto',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
