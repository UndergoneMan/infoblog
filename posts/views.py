from django.shortcuts import render

# Create your views here.
from posts.models import Post


def post_page(request):
    return render(request, 'index.html', {'posts': Post.objects.all()})
