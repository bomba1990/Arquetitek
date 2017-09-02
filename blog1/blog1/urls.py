from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

import blog.views as views
admin.autodiscover()


urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^$', views.index, name='index'),
                  url(r'^nosotros/$', views.nosotros, name='nosotros'),
                  url(r'^servicios/$', views.servcios, name='servicios'),
                  url(r'^portafolio/$', views.PortafolioView.as_view(), name='portafolio'),
                  url(r'^portafolio-detail/(?P<slug>[-\w]+)/$', views.PortaDetailView.as_view(), name='portafolio-detalle'),
                  url(r'^contacto/$', views.contacto, name='contacto'),
                  url(r'^blog$', views.Blog.as_view(), name='blog'),
                  url(r'^posts/(?P<slug>[-\w]+)/$', views.BlogDetailView.as_view(), name='post'),
                  url(r'^ckeditor/', include('ckeditor_uploader.urls')),
                  # url(r'^contactomail/$', views.contactomail, name='contactomail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)