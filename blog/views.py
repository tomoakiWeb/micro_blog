from django.shortcuts import render
from django.view.generic import ListView

from .modle import Blog


class BlogListView(ListView):
  model = Blog
