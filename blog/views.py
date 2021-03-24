from django.shortcuts import render, redirect
from .models import Post, Author

# Create your views here.
def index(request):
   tasks=Post.objects.all()
   


   
   context = {'tasks':tasks}
   return render(request,'blog/index.html',context)
   
def blogpost(request):
   tasks=Post.objects.all()
   


   
   context = {'tasks':tasks}
   return render(request,'blog/blogpost.html',context)

