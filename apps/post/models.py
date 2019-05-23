from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    commented_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
