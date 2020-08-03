from django.db import models


class Feed(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    feed = models.URLField()
    active = models.BooleanField(default=True)
    last_item = models.URLField(blank=True, null=True)
    channel = models.CharField(max_length=100)

    def __str__(self):
        return self.name
