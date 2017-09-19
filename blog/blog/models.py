from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def upload_fotos(instance, filename):
    return "{0}/{1}".format(type(instance).__name__.lower(), filename)


class Post(BaseModel):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    contenido = RichTextUploadingField()
    imagen = models.ImageField(upload_to=upload_fotos, blank=True)
    video = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True, editable=False)
    presentar = models.BooleanField(default=True)
    autor = models.ForeignKey(get_user_model())
    publicado = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.titulo)
        super(Post, self).save(*args, **kwargs)


class Foto(BaseModel):
    post = models.ForeignKey(Post)
    titulo = models.CharField(max_length=100)
    foto = models.ImageField(upload_to=upload_fotos, blank=True)

    def __str__(self):
        return self.titulo

class Portafolio(BaseModel):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    contenido = RichTextUploadingField()
    imagen = models.ImageField(upload_to=upload_fotos, blank=True)
    video = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(editable=False)
    presentar = models.BooleanField(default=True)
    autor = models.ForeignKey(get_user_model())
    create = models.CharField(max_length=200)
    completed = models.DateField()
    skills = models.CharField(max_length=200)
    client = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.titulo)
        super(Portafolio, self).save(*args, **kwargs)


class Photos(BaseModel):
    portafolio = models.ForeignKey(Portafolio)
    titulo = models.CharField(max_length=100)
    foto = models.ImageField(upload_to=upload_fotos, blank=True)

    def __str__(self):
        return self.titulo


