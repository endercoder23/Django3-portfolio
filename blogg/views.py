from django.shortcuts import render, get_object_or_404
from .models import blog

# Create your views here.
def all_bloggs(request):
    blogs = blog.objects.order_by('-date')
    return render(request, 'blogg/all_bloggs.html',{'blogs':blogs})

def detail(request, blog_id):
    blogg = get_object_or_404(blog, pk=blog_id)
    return render(request, 'blogg/detail.html',{'blogg':blogg})