from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from posts.models import Post
from posts.serializers import PostSerializer


def post_page(request):
    return render(request, 'index.html', {'posts': Post.objects.all()})

class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
