from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Show(models.Model):
    artist = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    zipcode = models.CharField(max_length=200)
    description = models.TextField()
    added_date = models.DateTimeField(blank=True,null=True)
    display_artist = models.CharField(max_length=200)
    display_city = models.CharField(max_length = 200)
    def publish(self):
        self.added_date = timezone.now()
        self.save()

    def __str__(self):
        return self.artist