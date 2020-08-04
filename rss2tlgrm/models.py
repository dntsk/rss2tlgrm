from django.db import models


class Feed(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    feed = models.URLField()
    active = models.BooleanField(default=True)
    channel = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField()
    date = models.DateTimeField(auto_now=True)
