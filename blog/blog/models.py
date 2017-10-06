from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def upload_fotos(instance, filename):
    return "{0}/{1}".format(type(instance).__name__.lower(), filename)


class Post(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = RichTextUploadingField()
    image = models.ImageField(upload_to=upload_fotos, blank=True)
    video = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True, editable=False)
    author = models.ForeignKey(get_user_model())
    published = models.DateField()

    class Meta:
        ordering = ["-published"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)[:50]
        super(Post, self).save(*args, **kwargs)


class PostPhoto(BaseModel):
    post = models.ForeignKey(Post)
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=upload_fotos, blank=True)

    def __str__(self):
        return self.title


class Portfolio(BaseModel):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to=upload_fotos)
    video = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(editable=False)
    author = models.ForeignKey(get_user_model())
    created_by = models.CharField(max_length=200)
    completed = models.DateField()
    services = models.CharField(max_length=200)
    client = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_services(self):
        return self.services.split(",")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)[:50]
        super(Portfolio, self).save(*args, **kwargs)


class PhotoPortfolio(BaseModel):
    portfolio = models.ForeignKey(Portfolio)
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=upload_fotos, blank=True)

    def __str__(self):
        return self.title
