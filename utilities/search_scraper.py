import urllib.request
import urllib.parse
import json
import time
from author_parser import AuthorParser

class SearchScraper:
    def __init__(self, search_terms):
        self.search_terms = search_terms

    def search_url(self, page):
      # https://oeis.org/search?q=keyword%3atabl%20author%3akagey&fmt=json
        uri = "https://oeis.org/search?q=" + urllib.parse.quote(self.search_terms) + "&fmt=json" + "&start=" + str(page*10)
        return uri

    def search_json(self, page=0):
        fp = urllib.request.urlopen(self.search_url(page))
        response_bytes = fp.read()
        response_text = response_bytes.decode("utf8")
        fp.close()
        return json.loads(response_text)

    def write_to_file(self, new_line):
        f = open("search_results2.txt", "a")
        f.write(new_line + "\n")
        f.close()


    def sequences_on_page(self, json_data):
      sequences = {}
      if json_data["count"] > 0:
        for seq_data in json_data["results"]:
          a_number = "A" + str(seq_data["number"]).zfill(6)
          author_string = AuthorParser(a_number, seq_data["author"]).full_string
          self.write_to_file(author_string)
          sequences[a_number] = author_string
      return sequences

    def all_sequences(self):
      page_results = self.search_json()
      page_count = page_results["count"]//10
      self.write_to_file(str(page_count + 1) + " pages:")
      sequences = self.sequences_on_page(page_results)
      for i in range(page_count):
        print(str(i + 2) + " of " + str(page_count + 1))
        self.write_to_file(str(i + 2) + " of " + str(page_count + 1))
        json = self.search_json(i + 1)
        sequences.update(self.sequences_on_page(json))
        time.sleep(10) # Throttle requests so that the OEIS servers aren't hit too hard.
      return sequences

# Search #1 was (probably):
#   link:rows,n keyword:tabl
# Search #2:
#   keyword:tabl link:Table,of -link:rows,n author:2017|author:2018|author:2019|author:2020
SearchScraper("keyword:tabl link:Table,of -link:rows,n author:2017|author:2018|author:2019|author:2020").all_sequences()
