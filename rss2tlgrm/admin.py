from django.contrib import admin
from .models import Feed, Post


class FeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'feed', 'channel', 'active')


class PostAdmin(admin.ModelAdmin):
    list_display = ('url', 'date')


admin.site.register(Feed, FeedAdmin)
admin.site.register(Post, PostAdmin)
