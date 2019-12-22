from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Post


def home(request):
    # context = {
    #     'posts': Post.objects.all()
    # }
    return render(request, 'blog/home.html', {'context':'home'})
    # return HttpResponse(request,"<h1>Home</h1>")


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
