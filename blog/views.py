from django.shortcuts import render

#dummy data

posts = [
    {
        'author' : 'CoreyMS',
        'title' : 'Blog Post 1',
        'content' : 'First Post content',
        'date_posted' : 'August 27, 2018'
    },
    {
        'author' : 'CoreyMS',
        'title' : 'Blog Post 1',
        'content' : 'First Post content',
        'date_posted' : 'August 27, 2018'
    }
]

def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')