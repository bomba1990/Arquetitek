from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils import timezone


# Create your models here.
class UserProfile(models.Model):
    nombre = models.CharField(max_length=300)
    usuario = models.OneToOneField(User)

    def __str__(self):
        return '%s' % self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    contenido = RichTextUploadingField()
    imagen = models.ImageField(upload_to="blog/fotos/", blank=True)
    video = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(editable=False)
    presentar = models.BooleanField(blank=True, null=False, default=True)
    autor = models.ForeignKey(UserProfile)
    publicado = models.DateField(default=timezone.now())

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(Post, self).save(*args, **kwargs)

    def publicacion(self):
        self.plublicado = timezone.now()
        self.save()


class Portafolio(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    contenido = RichTextUploadingField()
    imagen = models.ImageField(upload_to="blog/fotos/portafolio", blank=True)
    video = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(editable=False)
    presentar = models.BooleanField(blank=True, null=False, default=True)
    autor = models.ForeignKey(UserProfile)
    create = models.CharField(max_length=200)
    completed = models.DateField(default=timezone.now())
    skills = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    publicado = models.DateField(default=timezone.now())

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(Portafolio, self).save(*args, **kwargs)

    def publicacion(self):
        self.plublicado = timezone.now()
        self.save()


class Photos(models.Model):
    portafolio = models.ForeignKey(Portafolio)
    titulo = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="blog/fotos/portafolio", blank=True)

    def __str__(self):
        return self.titulo


class Foto(models.Model):
    post = models.ForeignKey(Post)
    titulo = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="blog/fotos/", blank=True)

    def __str__(self):
        return self.titulo


