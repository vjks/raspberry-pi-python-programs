import re

enteredRegex = input("Enter a regular expression:")
#enteredRegex = 'java$'
#print(enteredRegex)

fileHandler = open('mbox.txt')
count = 0

for line in fileHandler:
  line = line.rstrip()
  if re.search(enteredRegex, line):
    count = count + 1
    print(line)

print('mbox.txt had ' + str(count) + ' lines that matched ' + str(enteredRegex))
