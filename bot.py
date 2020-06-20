import tweepy
import time
from api_keys import consumer_key, consumer_secret, access_key, access_secret
from quotes import quotes

# auth with the api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

for quote in quotes:
    api.update_status(quote) # tweet the quote
    print(f"NEW TWEET: {quote}") # show tweet in terminal
    time.sleep(28800) # wait 28800 seconds = 8 hours
