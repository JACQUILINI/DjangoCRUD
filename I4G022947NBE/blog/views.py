from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView  
from  .models import Post

# Create your views here.

class createblogview (CreateView):
    model = Post
    fields: "__all__"
    success_url = reverse_lazy("blog:all")