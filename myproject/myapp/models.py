from django.db import models

# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=250, help_text="sarlavha kriting")
    body=models.TextField(help_text=" text kiriting")
    def __str__(self):
        return self.title