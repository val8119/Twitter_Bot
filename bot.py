import tweepy
import time
from api_keys import consumer_key, consumer_secret, access_key, access_secret
from quotes import quotes  # had to remove some in the pythonanywhere version cuz python2

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

for quote in quotes:
    api.update_status(quote)
    print(f"NEW TWEET: {quote}")
    # print("NEW TWEET: ", quote) pythonanywhere.com version cuz python2
    time.sleep(28800)
