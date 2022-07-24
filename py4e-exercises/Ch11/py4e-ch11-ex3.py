import re

filename = input("Enter the file name:")
revisionTotal = 0
count = 0

fileHandler = open(filename)
for line in fileHandler:
  line = line.rstrip()
  revisionList = re.findall('New Revision: ([0-9]+)', line)
  if len(revisionList) > 0:
      for revisionNumber in revisionList:
          revisionTotal = revisionTotal + int(revisionNumber)
          count = count + 1
print(int(revisionTotal/count))
