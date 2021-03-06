# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post
# posts = [
#     {
#         'author':'CoreyMS',
#         'title':'Blog Post 1',
#         'content': 'First post content',
#         'date_posted':'August 27, 2018'
#     },
#         {
#         'author':'Jane D\'arc',
#         'title':'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted':'August 28, 2018'
#     }
# ]
def home(request):
    context = {
        'title':'Home',
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context=context)

def about(request):
    return render(request,'blog/about.html',context={'title':'About' })