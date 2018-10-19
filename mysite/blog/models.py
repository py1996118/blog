from django.db import models

class BlogPost(models.Model):
    """docstring for BlogPost"""
    title = models.CharField(max_length =150)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
