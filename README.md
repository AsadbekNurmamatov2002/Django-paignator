# Django-paignator


![image](https://github.com/AsadbekNurmamatov2002/Django-paignator/assets/144318530/32edc9f2-8243-4a09-baa9-a1dcbd2c524a)

__myproject>sittengs.py__
![image](https://github.com/AsadbekNurmamatov2002/Django-paignator/assets/144318530/eda99fa0-2105-4608-8452-efb2b1c934c5)
![image](https://github.com/AsadbekNurmamatov2002/Django-paignator/assets/144318530/001bc60c-e650-4e78-a417-d783faa842d0)
![image](https://github.com/AsadbekNurmamatov2002/Django-paignator/assets/144318530/a2c6528f-f300-4a0c-8a48-624c315b1fc8)

__myproject>urls.py__
>      from django.contrib import admin
>      from django.urls import path, include
>
>      urlpatterns = [
>          path('admin/', admin.site.urls),
>          path('', include('myapp.urls')),
>      ]
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


__templates>index.html__

>      <!DOCTYPE html>
>      <html lang="en">
>      <head>
>         <meta charset="UTF-8">
>         <meta name="viewport" content="width=device-width, initial-scale=1.0">
>          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384->      >      >      >      EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
>      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" >      crossorigin="anonymous"></script>
>          <title>Document</title>
>      </head>
>      <body>
>      
>        {% for i in post %}
>        <h1>{{ i.title }}</h1><br>
>        <p>{{ i.body }}</p>
>        {% endfor %}
>        <!-- disabled -->
>        <!-- tabindex="-1" aria-disabled="true" -->
>          <nav aria-label="...">
>              <ul class="pagination">
>                {% if post.has_previous %}
>                <li class="page-item ">
>                  <a class="page-link" href="{{ request.path }}?page={{ post.previous_page_number }}" >Previous</a>
>                </li>
>                {% endif %}
>                {% if page.number > 3 %}
>                        <li class="page-item">
>                          <a class="page-link" href="{{ request.path }}?page=1">1</a>
>                        </li>
>                {% endif %}
>      
>                {% for i in post.paginator.page_range %}
>                      {% if post.number == i %}
>                        <li class="page-item active">
>                          <span class="page-link">
>                            {{ i }}
>                            <span class="sr-only"></span>
>                          </span>
>                        </li>
>                        {% elif i > post.number|add:'-3' and i < post.number|add:'3' %}
>                          <li class="page-item">
>                            <a class="page-link" href="{{ request.path }}?page={{ i }}">{{ i }}</a>
>                          </li>
>                      {% endif %}
>                    {% endfor %}
>      
>                {% if post.has_next %}
>                <li class="page-item">
>                  <a class="page-link" href="{{ request.path }}?page={{ post.next_page_number }}">Next</a>
>                </li>
>                {% endif %}
>              </ul>
>            </nav>
>      </body>
>      </html>
