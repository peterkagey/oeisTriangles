import json
from datetime import datetime

# JSONAccountant reads data.json, and randomly picks an unseen value, and moves it to the seen collection.
class JSONAccountant:
  def __init__(self):
    self.file_location = "data.json"
    self.data = json.loads(open(self.file_location, "r").read())
    self.unseen_sequences = self.data["unseen"]

  def get_todays_sequence(self):
    unseen_sequences = self.unseen_sequences
    todays_index = (datetime.now() - datetime(2021,4,5)).days
    return (self.unseen_sequences[todays_index][0], self.unseen_sequences[todays_index][1])
