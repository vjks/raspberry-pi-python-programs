fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
    
dow = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len( words ) > 0 and words[ 0 ] == 'From':
        dow[ words[ 2 ] ] = dow.get(words[2],0) + 1
        
print(dow)
    