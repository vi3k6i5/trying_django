from django.db import models

# Create your models here.
class Tweet(models.Model):
    tweet_text = models.CharField(max_length=140)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.tweet_text