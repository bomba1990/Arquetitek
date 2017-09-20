from .models import Post, Portfolio


def content_portfolio(request):
    return {'content_portfolio': Portfolio.objects.all()[:4], 'content_post': Post.objects.all()[:4]}



