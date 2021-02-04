from django.shortcuts import render
from .models import*

def Index(request):
    posts = BlogPost.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'MainApp/index.html',context)
