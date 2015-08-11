from django.contrib import admin

# Register your models here.
from .models import Tweet

class TweetAdmin(admin.ModelAdmin):
    fields = ['tweet_text']

admin.site.register(Tweet, TweetAdmin)
