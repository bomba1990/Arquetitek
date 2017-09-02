from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^nosotros/$', views.nosotros, name='nosotros'),
    url(r'^servicios/$', views.servcios, name='servicios'),
    url(r'^portafolio/$', views.PortafolioView.as_view(), name='portafolio'),
    url(r'^portafolio-detail/(?P<slug>[-\w]+)/$', views.PortaDetailView.as_view(), name='portafolio-detalle'),
    url(r'^contacto/$', views.contacto, name='contacto'),
    url(r'^blog$', views.Blog.as_view(), name='blog'),
    url(r'^posts/(?P<slug>[-\w]+)/$', views.BlogDetailView.as_view(), name='post'),
]