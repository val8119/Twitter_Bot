import tweepy
import time
from quotes import quotes  # had to remove some in the pythonanywhere version cuz python2

CONSUMER_KEY = "zimr3hIT1L5Q2UpTqe0N9n2AD"
CONSUMER_SECRET = "KUCz5c9q9IF1xqZpoNXBrYRBoQwym11vpQgJNYFZWdu0CSoWsj"
ACCESS_KEY = "1163483862279905282-B7l2smCk2wB31ZDHFoPqn7HhaUAt1a"
ACCESS_SECRET = "bGXyH02keytfyWfwqqWMS8Mn5QH7mrvtnrlqRcF014UkR"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

for quote in quotes:
    api.update_status(quote)
    print(f"NEW TWEET: {quote}")
    # print("NEW TWEET: ", quote) pythonanywhere.com version cuz python2
    time.sleep(28800)
