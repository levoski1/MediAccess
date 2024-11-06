from django.db import models
# from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    class Meta:
        verbose_name = 'Blog post'
        verbose_name_plural = 'posts' 

    def __str__(self) -> str:
        return self.title
    

class Comment(models.Model):
    fname = models.CharField(max_length=60)
    lname = models.CharField(max_length=40)
    email = models.EmailField()
    body = models.TextField(default='Default comment body')
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.fname + ' ' + self.lname