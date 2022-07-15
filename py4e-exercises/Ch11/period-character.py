# Search for all lines that begin with F followed by any two characters followed by m and then colon, and prints them.

import re
fileHandler = open('mbox-short.txt')
for line in fileHandler:
  line = line.rstrip()
  if re.search('^F..m:', line):
      print( line )
