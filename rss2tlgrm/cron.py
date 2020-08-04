import time

import feedparser
import telebot
import os

from django_cron import CronJobBase, Schedule
from .models import Feed, Post


class FetchRSS(CronJobBase):
    RUN_EVERY_MINS = 5

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'rss2tlgrm.parser'

    def do(self):
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
                        # bot.send_message(f'@{f.channel}', message)
                        # time.sleep(10)
            else:
                print(f'Skipping "{f.name}" due to not active.')