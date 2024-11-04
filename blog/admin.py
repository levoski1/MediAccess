from django.contrib import admin
from .models import Post, Comment, Category

class PostModel(admin.ModelAdmin):
    pass

class CommmentModel(admin.ModelAdmin):
    pass

class CategoryModel(admin.ModelAdmin):
    pass

admin.site.register(Post, PostModel)
admin.site.register(Comment, CommmentModel)
admin.site.register(Category, CategoryModel)
