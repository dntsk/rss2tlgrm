import time
import feedparser
import telebot
import os

from django.core.management.base import BaseCommand, no_translations

from rss2tlgrm.models import Feed, Post


class Command(BaseCommand):
    help = 'Check RSS feeds'

    @no_translations
    def handle(self, *args, **options):
        bot = telebot.TeleBot(os.getenv("TGBOT_TOKEN"))
        feeds = Feed.objects.all()
        for f in feeds:
            if f.active:
                print(f'Processing {f.name}.')
                d = feedparser.parse(f.feed)
                for i in d.entries[:20]:
                    try:
                        p = Post.objects.get(url__exact=i.link)
                    except Post.DoesNotExist:
                        p = None
                    if p is None:
                        link = i.link.split('?')[0]
                        print(f'{f.channel}: {i.title} {link}')
                        p = Post(url=i.link)
                        p.save()
                        message = f"{i.title}\n\n{link}"
                        bot.send_message(f'@{f.channel}', message)
                        time.sleep(2)
            else:
                print(f'Skipping "{f.name}" due to not active.')
