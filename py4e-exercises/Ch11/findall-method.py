# Extract all the emails from a Document
# Email beings with a letter followed by any number of non-space characters, followed by an @ sign, followed by any
# number of letters, followed by a period, followed by any number of letters
import re
fileHandler = open('mbox-short.txt')
for line in fileHandler:
    line = line.rstrip()
    myList = re.findall( '[A-Za-z]\S+@\S+\.\S*[A-Za-z]', line )
    if len(myList) != 0:
        print( myList )
