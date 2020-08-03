import time

import feedparser
import telebot
import os

from django_cron import CronJobBase, Schedule
from .models import Feed, Channel


class FetchRSS(CronJobBase):
    RUN_EVERY_MINS = 5

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'rss2tlgrm.parser'

    def do(self):
        bot = telebot.TeleBot(os.getenv("TOKEN"))
        feeds = Feed.objects.all()
        for f in feeds:
            channel = Channel.objects.get(pk=f.channel_id)
            d = feedparser.parse(f.feed)
            for i in d.entries:
                if i.link != f.last_item:
                    link = i.link.split('?')[0]
                    print(f'{channel.tg_id}: {i.title} {link}')
                    message = f"{i.title}\n\n{link}"
                    # bot.send_message(f'@{channel.tg_id}', message)
                    time.sleep(1)
                else:
                    break
            f.last_item = d.entries[0].link
            f.save()
