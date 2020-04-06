from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=50, verbose_name='Category Name')
    cat_desc = models.TextField(blank=True, verbose_name='Category Description')

    def __str__(self):
        return self.cat_name

class Post(models.Model):
    pst_title = models.CharField(max_length=150, verbose_name='Post Title')
    pst_img = models.ImageField(null=True, upload_to='img_uploads', blank=True, verbose_name='Post Image')
    created_date = models.DateTimeField(default=timezone.now)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    cat = models.ManyToManyField(Category, verbose_name='Category')
    content = models.TextField()

    def __str__(self):
        return self.pst_title

class About(models.Model):
    abt_title = models.CharField(max_length=160, verbose_name='Member Name')
    abt_img  = models.ImageField(blank=True, upload_to='img_uploads', verbose_name='About Image')
    abt_content = models.TextField(blank=True, verbose_name='About Content')


    def __str__(self):
        return self.abt_title

class Service(models.Model):
    srv_title = models.CharField(max_length=150, verbose_name='Service Title')
    srv_content = models.TextField(blank=True, verbose_name='Service Content')

    def __str__(self):
        return self.srv_title






