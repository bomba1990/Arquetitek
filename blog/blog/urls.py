from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^nosotros/$', views.us, name='us'),
    url(r'^servicios/$', views.services, name='services'),
    url(r'^portafolio/$', views.PortfolioView.as_view(), name='portfolio'),
    url(r'^portafolio-detail/(?P<slug>[-\w]+)/$', views.PortfolioDetailView.as_view(), name='portfolio-detail'),
    url(r'^contacto/$', views.contact, name='contact'),
    url(r'^blog$', views.Blog.as_view(), name='blog'),
    url(r'^posts/(?P<slug>[-\w]+)/$', views.BlogDetailView.as_view(), name='post'),

]
