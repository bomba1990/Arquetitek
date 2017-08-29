from .models import Post, Portafolio


def mis_variables(request):
    return {'mis_variables': Portafolio.objects.all}


def mis_post(request):
    return {'mis_post': Post.objects.all}

