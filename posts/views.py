from django.shortcuts import render

# Create your views here.

def post_page(request):
    return render(request, 'index.html')