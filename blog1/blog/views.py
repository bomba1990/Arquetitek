from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext, context
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView
from .forms import Formulario
from .models import Post, Foto, Portafolio, Photos
from django.views.generic.list import ListView
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.contrib import messages
from django.template.loader import render_to_string

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


def contacto(request):
    if request.method == 'POST':
        formulario = Formulario(request.POST)
        if formulario.is_valid():
            asunto = 'Mensaje de Arquetitek'
            nombre = formulario.cleaned_data['nombre']
            email = formulario.cleaned_data['email']
            telefono = formulario.cleaned_data['telefono']
            mensaje = formulario.cleaned_data['mensaje']
            ctx = {'nombre': nombre, 'email': email, 'telefono': telefono, 'mensaje': mensaje}
            message_html = render_to_string('datos_email_admin', ctx)
            mail = EmailMultiAlternatives(asunto, message_html, to=['juniorrivasmendoza@gmail.com'])
            mail.attach_alternative(message_html, 'text/html')
            mail.send()
        return HttpResponseRedirect('/')
    else:
        formulario = Formulario()
        messages.success(request, 'Profile details updated.')

    return render(request, 'contacto.html', {'formulario': formulario})


# def contacto(request):
#     if request.method == 'POST':
#         form = Formulario(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('contacto.html')
#     else:
#         form = Formulario()
#     return render(request, 'contacto.html', {'form': form})


# def contacto(request):
#     if request.method == 'POST':
#         form = Formulario(request.POST)
#         if form.is_valid():
#             asunto = 'Mensaje de Arquetitek'
#             nombre = form.cleaned_data['nombre']
#             telefono = form.cleaned_data['telefono']
#             mensaje = form.cleaned_data['mensaje']
#             mail = EmailMessage(asunto, mensaje, nombre, telefono, to=['juniorrivasmendoza@gamil.com'])
#             mail.send()
#         return HttpResponseRedirect('index.html')
#     else:
#         form = Formulario(initial={'mensaje': '¡Adoro tu sitio!'})
#     return render(request, 'contacto.html', {'form': form})
