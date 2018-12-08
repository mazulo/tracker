from django.contrib.postgres.fields import ArrayField
from django.db import models

from .tracker import TwitterApi


class TrackFollowers(models.Model):
    follower_list = ArrayField(
        models.CharField(max_length=50, blank=True)
    )
    unfollowers = ArrayField(
        models.CharField(max_length=50, blank=True),
        null=True,
    )

    def get_twitter_follower_list(self):
        twitter = TwitterApi()

        return twitter.get_followers()

    def update_unfollowers(self):
        twitter = TwitterApi()
        updated_followers = twitter.get_followers()
        unfollowers = set(self.follower_list) - set(updated_followers)

        if unfollowers:
            self.follower_list = updated_followers
            self.unfollowers = list(unfollowers)
            self.save()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.follower_list = self.get_twitter_follower_list()

        super().save(*args, **kwargs)
