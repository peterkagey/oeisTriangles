import re
from datetime import datetime
# _Lynette O'Brien_, Dec 15 2016
#  => Lynette O'Brien in December 2016.
# _N. J. A. Sloane_ and _J. H. Conway_
#  => N. J. A. Sloane and J. H. Conway
# _Michael De Vlieger_, _Peter Kagey_, _Antti Karttunen_, _Robert G. Wilson v_, May 09 2020
#  => Michael De Vlieger, Peter Kagey, Antti Karttunen, and Robert G. Wilson v in May 2020.

# Parses the author line on the OEIS.
class AuthorParser:
  def __init__(self, sequence, author_string):
    self.raw_author = author_string
    self.date_regex = re.compile('\w{3} \d+ \d{4}')
    self.authors_regex = re.compile('_([\w\.,\' ]+?)_')
    self.full_string = "Sequence " + sequence + " was added to the OEIS" + self.get_authors() + self.get_date()

  def get_date(self):
    date_match = self.date_regex.search(self.raw_author)
    if date_match == None:
      return "."
    else:
      raw_date_string = date_match.group()
      date = datetime.strptime(raw_date_string,"%b %d %Y").date()
      return date.strftime(" in %B %Y.")

  def get_authors(self):
    authors = self.authors_regex.findall(self.raw_author)
    number_of_authors = len(authors)
    if number_of_authors == 1:
      return " by " + authors[0]
    if number_of_authors == 2:
      return " by " + authors[0] + " and " + authors[1]
    if number_of_authors == 3:
      return " by " + authors[0] + ", " + authors[1] + ", and " + authors[2]
    if number_of_authors == 4:
      return " by " + authors[0] + ", " + authors[1] + ", " + authors[2] + ", and " + authors[3]
    if number_of_authors == 5:
      return " by " + authors[0] + ", " + authors[1] + ", " + authors[2] + ", " + authors[3] + ", and " + authors[2]
    else:
      return ""
