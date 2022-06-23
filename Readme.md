[![Logo](https://dntsk.dev/assets/logo_transparent_crop_360.png)](https://dntsk.dev)

[![Maintained](https://img.shields.io/badge/maintained%20by-dntsk.dev-blue.svg)](https://dntsk.dev/) [![GitHub tag](https://img.shields.io/github/tag/dntsk/rss2tlgrm.svg)](https://github.com/dntsk/rss2tlgrm/tags/) [![MIT license](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

# RSS2TLGRM - RSS to Telegram selfhosted bot

## Description

RSS2TLGRM is a selfhosted bot that converts RSS feeds to Telegram posts.

## Getting Telegram bot token

1. Open Telegram
2. Search @ botfather
3. Type /newbot .
4. It will show “Alright, a new bot. How are we going to call it? Please choose a name for your bot.”
5. Type the name of your bot.
6. After, it’ll show “Good. Now let’s choose a username for your bot. It must end in `bot`. Like this, for example: TetrisBot or tetris_bot.”
7. You’ve to give a unique username and it should be ending with bot.
8. After giving the name it’ll show token.

You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you’ve finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

## Getting Started

You may use docker-compose.yml as example to run the bot on your host. Don't forget to change environment variables.

Right after run you need to register admin account:

```bash
docker-compose exec -ti rss2tlgrm ./manage.py createsuperuser
```

Open your bot URL in browser adding `/admin/` in the end and login with admin account.

Your URL should look like this: https://rss.example.com/admin/

## Have it working

Create new channel and add your bot to it as administrator with write permissions. It doesn't need more permissions, just write messages in channel.

Login to the bot's admin URL with created admin account and add your RSS feeds with posting to your channel.
