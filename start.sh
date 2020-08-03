#!/bin/sh

./manage.py migrate --noinput
crond
gunicorn --bind :8000 --workers 3 rss2tlgrm.wsgi:application
