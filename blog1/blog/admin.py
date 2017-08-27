from django.contrib import admin

from .models import Post, UserProfile, Foto, Portafolio, Photos


# Register your models here.

class FotoInline(admin.TabularInline):
    model = Foto


class PostAdmin(admin.ModelAdmin):
    inlines = [FotoInline, ]
    list_display = ['titulo', 'imagen', 'publicado', 'autor']


class PhotosInline(admin.TabularInline):
    model = Photos


class PostAdminPhoto(admin.ModelAdmin):
    inlines = [PhotosInline, ]
    list_display = ['titulo', 'imagen', 'publicado', 'autor']

admin.site.register(UserProfile)
admin.site.register(Post, PostAdmin)
admin.site.register(Portafolio, PostAdminPhoto)
