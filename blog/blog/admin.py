from django.contrib import admin

from .models import Post, PostPhoto, Portfolio, PhotoPortfolio


# Register your models here.

class PhotoInline(admin.TabularInline):
    model = PostPhoto


class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]
    list_display = ['title', 'image', 'published', 'author']


class PhotoPortfolioInline(admin.TabularInline):
    model = PhotoPortfolio


class PortfolioAdmin(admin.ModelAdmin):
    inlines = [PhotoPortfolioInline, ]
    list_display = ['title', 'image', 'author']

admin.site.register(Post, PostAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
