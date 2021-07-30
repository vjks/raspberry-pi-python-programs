fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
    
fromEmailAddress = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len( words ) > 0 and words[ 0 ] == 'From':
        fromEmailAddress[ words[ 1 ] ] = fromEmailAddress.get(words[1],0) + 1
        
print(fromEmailAddress)