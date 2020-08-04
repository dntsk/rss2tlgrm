from django.contrib import admin
from .models import Feed


class FeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'feed', 'channel', 'active')


admin.site.register(Feed, FeedAdmin)
