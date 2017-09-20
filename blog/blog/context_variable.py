from .models import Post, Portfolio


def content_portfolio(request):
    return {'context_portfolio': Portfolio.objects.all()[:4], 'context_post': Post.objects.all()[:4]}



