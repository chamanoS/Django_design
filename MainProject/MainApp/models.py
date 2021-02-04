from django.db import models
from django.contrib.auth.models import User


class BlogCategory(models.Model):
    title = models.CharField( max_length=200, default="Uncategories")
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='MainProject',null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateField( auto_now_add=True)
    updated_at = models.DateField( auto_now=True)


    def __str__(self):
        return self.title


class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='MainProject',null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateField( auto_now_add=True)
    updated_at = models.DateField( auto_now=True)


    def __str__(self):
        return self.title
    
