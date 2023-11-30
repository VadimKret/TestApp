from django.shortcuts import render
from django.http import HttpRequest

from posts.models import Posts

def page_posts(reqwests):
    posts = Posts.objects.all()

def posts(requests):
    return render(request, posts.html)
# Create your views here.
