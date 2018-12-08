import twitter
from decouple import config


class TwitterApi:

    def __init__(self):
        self.client = twitter.Api(
            consumer_key=config('API_KEY'),
            consumer_secret=config('API_SECRET_KEY'),
            access_token_key=config('ACCESS_TOKEN'),
            access_token_secret=config('ACCESS_TOKEN_SECRET'),
        )

    def get_followers(self):
        followers = list(
            [follower.screen_name for follower in self.client.GetFollowers()]
        )

        return followers
