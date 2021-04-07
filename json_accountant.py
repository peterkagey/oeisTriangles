import json
from datetime import datetime

# JSONAccountant reads data.json, and randomly picks an unseen value, and moves it to the seen collection.
class JSONAccountant:
  def __init__(self):
    self.unseen_sequences = json.loads(open("data.json", "r").read())

  def get_todays_sequence(self):
    todays_index = (datetime.now() - datetime(2021,4,5)).days
    [a_number, tweet_copy] = self.unseen_sequences[todays_index]
    return (a_number, tweet_copy)
