from django.shortcuts import render
from django.shortcuts import get_object_or_404
from blog.models import Post

def index(request):
    posts = Post.objects.all()

    return render(request, 'index.html', {
        'posts': posts
    })


def about(request):
    return render(request, 'about.html')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'post_detail.html', {
        'post': post
    })