from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=65)
    slug = models.SlugField(max_length=65)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/category/{self.slug}/'

    
class Author(models.Model):
    name = models.CharField(max_length=65)
    slug = models.SlugField(max_length=65)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/author/{self.slug}/'

class Recipe(models.Model):

    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField(max_length=65)

    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    is_published = models.BooleanField(default=False)    
    
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,null=True,blank=True,default=None
    )
    
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL,null=True,blank=True,default=None
    )
    
    def __str__(self):
        return self.title
    
    def is_recent(self):
        from django.utils import timezone
        from datetime import timedelta

        if self.creation_date >= timezone.now() - timedelta(days=7):
            return True
        return False
    
    def get_preparation_steps_as_list(self):
        return self.preparation_steps.splitlines()
    
    def get_absolute_url(self):
        return f'/recipes/{self.slug}/'