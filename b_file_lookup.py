import urllib.request
# Copied from table_parity project.

class BFileLookup:
    def __init__(self, sequence_name):
        self.sequence_name = sequence_name

    def b_file_url(self):
        return "http://oeis.org/" + self.sequence_name + "/b" + self.sequence_name[1:] + ".txt"

    def b_file_txt(self):
        fp = urllib.request.urlopen(self.b_file_url())
        b_file_bytes = fp.read()
        b_file_text = b_file_bytes.decode("utf8")
        fp.close()
        return b_file_text
