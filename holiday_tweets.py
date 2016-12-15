import tweepy
from time import sleep
import os

api_key = os.environ['api_key']
api_secret = os.environ['api_secret']
access_token_key = os.environ['access_token_key']
access_token_secret = os.environ['access_token_secret']

OAUTH_KEYS = {'consumer_key': api_key,
              'consumer_secret': api_secret,
              'access_token_key': access_token_key,
              'access_token_secret': access_token_secret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'],
                           OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)


def hashtag(tweet, num_items):

    cricTweet = tweepy.Cursor(api.search, q=tweet).items(num_items)

    return list(cricTweet)


def get_html(id, wait=0):
    sleep(wait)
    cricTweet = api.get_oembed(id=id)['html']

    return cricTweet
