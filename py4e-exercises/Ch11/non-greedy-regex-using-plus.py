# Search for lines that start with From and have an at sign
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@?', line): # The expression is made non-greedy by adding a ? after the + sign.
        print(line)