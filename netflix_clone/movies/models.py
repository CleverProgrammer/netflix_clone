from django.db import models

# Create your models here
class Movie(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    synopsis = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(null=True)
    video_link = models.URLField(max_length=1000, null=True)

    def __str__(self):
        return self.title

