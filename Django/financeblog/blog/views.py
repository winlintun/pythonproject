from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.


def list_blogs(request):
	blogs = Blog.objects.all()
	return render(request, 'blog/list.html', {'blog':blogs})


def detail_blog(request):
	blog = get_object_or_404(Blog, pk=pk)
	return render(request, "blog/detail.html", {'blog':blog})