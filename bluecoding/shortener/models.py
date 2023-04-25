from django.db import models

class ShortenedURL(models.Model):
    short_url = models.CharField(max_length=100, unique=True)
    long_url = models.TextField()

    def __str__(self):
        return self.short_url
