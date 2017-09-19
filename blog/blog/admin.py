from django.contrib import admin

from .models import Post, Foto, Portafolio, Photos


# Register your models here.

class FotoInline(admin.TabularInline):
    model = Foto


class PostAdmin(admin.ModelAdmin):
    inlines = [FotoInline, ]
    list_display = ['titulo', 'imagen', 'publicado', 'autor']


class PhotosInline(admin.TabularInline):
    model = Photos


class PortafolioAdmin(admin.ModelAdmin):
    inlines = [PhotosInline, ]
    list_display = ['titulo', 'imagen', 'autor']

admin.site.register(Post, PostAdmin)
admin.site.register(Portafolio, PortafolioAdmin)
