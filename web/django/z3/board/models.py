from django.db import models
from users.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    has_comment = models.BooleanField(default=True)  # 답변가능 여부

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('board:index', args=[self.name])

class Post(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    voter = models.ManyToManyField(User, related_name='voter')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_post')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
