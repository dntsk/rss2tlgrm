# Generated by Django 4.2.4 on 2023-08-30 08:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rss2tlgrm", "0003_remove_feed_last_item"),
    ]

    operations = [
        migrations.AddField(
            model_name="feed",
            name="publish_description",
            field=models.BooleanField(default=True),
        ),
    ]