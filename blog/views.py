from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView, DetailView

class Blog(ListView):
    model = Post
    template_name = 'blog/blog.html'