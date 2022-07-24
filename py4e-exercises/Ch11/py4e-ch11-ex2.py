import re

fileHandler = open('mbox.txt')
for line in fileHandler:
  line = line.rstrip()
  if re.search('New Revision: [0-9]+', line):
    print(line)
