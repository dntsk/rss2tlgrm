from django.db import models


class Feed(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    feed = models.URLField()
    active = models.BooleanField(default=True)
    last_item = models.URLField(blank=True, null=True)
    channel = models.ForeignKey(
        'Channel',
        on_delete=models.CASCADE,
        blank=True, null=True
    )

    def __str__(self):
        return self.name

class Channel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    tg_id = models.CharField(max_length=20)

    def __str__(self):
        return self.name