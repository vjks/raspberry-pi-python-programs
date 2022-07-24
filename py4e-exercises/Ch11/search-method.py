import re

fileHandler = open('mbox-short.txt')
for line in fileHandler:
  line = line.rstrip()
  if re.search('^X\S*: [0-9]+', line):
    print(line)
