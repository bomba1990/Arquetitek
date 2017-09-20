from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import DetailView
from django.views.generic.list import ListView

from .forms import Form
from .models import Post, PostPhoto, Portfolio, PhotoPortfolio


# Create your views here.
class Blog(ListView):
    model = Post
    template_name = 'blog.html'
    paginate_by = 6
    context_object_name = "post_list"


def get_queryset(self, **kwargs):
    return Post.objects.filter(presentar=True).order_by("-published")


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog-detalle.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context["gallery"] = PostPhoto.objects.filter(post=self.object)
        return context


class PortfolioView(ListView):
    model = Portfolio
    template_name = 'portfolio.html'
    paginate_by = 6


class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio-detail.html'

    def get_context_data(self, **kwargs):
        context = super(PortfolioDetailView, self).get_context_data(**kwargs)
        context["gallery"] = PhotoPortfolio.objects.filter(portfolio=self.object)
        return context


def index(request):
    return render(request, 'index.html')


def us(request):
    return render(request, 'nosotros.html', )


def services(request):
    return render(request, 'servicios.html', )


def contact(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            affair = 'Mensaje de Arquetitek'
            name = form.cleaned_data["name"]
            email = form.cleaned_data['email']
            phone = form.cleaned_data["phone"]
            message = form.cleaned_data["message"]
            ctx = {'name': name, 'email': email, 'phone': phone, 'message': message}
            message_html = render_to_string('datos_mail_admin.html', ctx)
            mail = EmailMultiAlternatives(affair, message_html, cc=(email,), to=['juniorrivasmendoza@gmail.com'])
            mail.attach_alternative(message_html, 'text/html')
            mail.send()
            messages.success(request, 'Su message fue enviado con Exito', extra_tags='alert')
            return HttpResponseRedirect('index.html')
        else:
            messages.warning(request, 'Please correct the error below.')
    else:
        form = Form()
    return render(request, 'contacto.html', {'form': form}, )
