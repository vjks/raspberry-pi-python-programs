import re
fileHandler = open('mbox-short.txt')
for line in fileHandler:
  line = line.rstrip()
  if re.search('^From:.+@', line):
    print(line)
