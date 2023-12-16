# Django-paignator


![image](https://github.com/AsadbekNurmamatov2002/Django-paignator/assets/144318530/32edc9f2-8243-4a09-baa9-a1dcbd2c524a)

__myapp>models.py__
>      from django.db import models
>
>      class Post(models.Model):
>          title=models.CharField(max_length=250, help_text="sarlavha kriting")
>          body=models.TextField(help_text=" text kiriting")
>          def __str__(self):
>             return self.title

__myapp>admin.py__

>      from django.contrib import admin
>      from .models import Post
>
>      @admin.register(Post)
>      class PostModel(admin.ModelAdmin):
>          list_display=['title','body']

__myapp>views.py__

>      from django.shortcuts import render
>      from .models import Post
>      from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
>
>      def home(request):
>         post=Post.objects.all()
>         page=request.GET.get('page', 1)
>         paginator=Paginator(post, 1 )
>         try:
>             post=paginator.page(page)
>         except PageNotAnInteger:
>             post=paginator.page(1)
>         except EmptyPage:
>             post=paginator.page(paginator.num_pages)
>         return render(request, 'index.html', {'post':post})

__myapp>urls.py__

>       from django.urls import path
>       from .views import home
> 
>       urlpatterns =[
>          path('', home, name="home"),
>       ]
