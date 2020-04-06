from django.contrib import admin
from correction_app.models import Category, Post, About, Service

# Register your models here.

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(About)
admin.site.register(Service)
