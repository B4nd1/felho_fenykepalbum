from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=48)
    body = models.TextField()
    slug = models.SlugField(max_length=48)
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.title