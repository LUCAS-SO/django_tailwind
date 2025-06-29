from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'app_blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5 

    def get_queryset(self):
        return Post.objects.filter(publicado=True)
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'app_blog/post_detail.html'
    context_object_name = 'post'