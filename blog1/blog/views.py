from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView, TemplateView

from blog.models import Post, Foto, Portafolio, Photos
from django.views.generic.list import ListView


# Create your views here.


class Blog(ListView):
    model = Post
    template_name = 'blog.html'
    paginate_by = 6
    context_object_name = "post_list"

    def get_queryset(self, **kwargs):
        return Post.objects.filter(presentar=True).order_by("-publicado")


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog-detalle.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context["galeria"] = Foto.objects.filter(post=self.object)
        return context


class PortafolioView(ListView):
    model = Portafolio
    template_name = 'portafolio.html'
    paginate_by = 6


class PortaDetailView(DetailView):
    model = Portafolio
    template_name = 'portafolio-detalle.html'

    def get_context_data(self, **kwargs):
        context = super(PortaDetailView, self).get_context_data(**kwargs)
        context["galeria"] = Photos.objects.filter(portafolio=self.object)
        return context


def index(request):
    return render(request, 'index.html', )


def nosotros(request):
    return render(request, 'nosotros.html', )


def servcios(request):
    return render(request, 'servicios.html', )


#
# def portafolio(request):
#     return render(request, 'portafolio.html', )


# def portafolio_detail(request):
#     return render(request, 'portafolio-detalle.html', )


def contacto(request):
    return render(request, 'contacto.html', )
