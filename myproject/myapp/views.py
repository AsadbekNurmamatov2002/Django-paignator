from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def home(request):
    post=Post.objects.all()
    page=request.GET.get('page', 1)
    paginator=Paginator(post, 1 )

    try:
        post=paginator.page(page)
    except PageNotAnInteger:
        post=paginator.page(1)
    except EmptyPage:
        post=paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'post':post})