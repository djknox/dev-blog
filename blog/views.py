from django.shortcuts import render
from blog.models import Post

def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')