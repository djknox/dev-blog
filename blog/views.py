from django.shortcuts import render
from django.shortcuts import get_object_or_404
from blog.models import Post, Tag

def index(request):
    posts = Post.objects.all()

    return render(request, 'index.html', {
        'posts': posts
    })


def about(request):
    return render(request, 'about.html')


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'post_detail.html', {
        'post': post
    })


def tag_detail(request, pk):
    tag = get_object_or_404(Tag, pk=pk)

    return render(request, 'tag_detail.html', {
        'tag': tag
    })