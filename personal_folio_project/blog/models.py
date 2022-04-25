from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
