from django.shortcuts import render
from .models import Post
#dummy data

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'August 29, 2018'
    }
]





def home(request):

    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'ohohoo'})