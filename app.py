from secrets import *
from oeis_drawer import OEISDrawer
from json_accountant import JSONAccountant
import tweepy

class TwitterPoster:
  def __init__(self):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    self.api = tweepy.API(auth)

api = TwitterPoster().api

def handler(event, context):
  if ("a_number" in event) and "tweet_copy" in event:
    a_number = event['a_number']
    tweet_copy = event['tweet_copy']
  else:
    accountant = JSONAccountant() # Get a new one each time, just in case.
    (a_number, tweet_copy) = accountant.get_todays_sequence()
  OEISDrawer(a_number).draw()
  file_with_path = "/tmp/" + a_number + ".png"
  api.update_with_media(filename=file_with_path, status=tweet_copy)
  return "Posted Tweet with message: '" + tweet_copy + "'"
