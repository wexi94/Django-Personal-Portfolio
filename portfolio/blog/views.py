from django.shortcuts import render , get_object_or_404
from .models import Blog
def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request , 'blogpost/all_blogs.html', {'blogs':blogs})
def detail(request, blog_id):
    blog = get_object_or_404(Blog , pk=blog_id)
    return render(request, 'blogpost/detail.html',{'blog': blog})
