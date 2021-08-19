fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
    
fromDomain = dict()
counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len( words ) > 0 and words[ 0 ] == 'From':
        #atpos = words[ 1 ].find( '@' ) # Find the position of the @ sign, the domain is after it.
        #host = words[ 1 ][ atpos + 1 : ]  #From one character after @ sign to the end of the string.
        #fromDomain[ host ] = fromDomain.get( host, 0 ) + 1
        #print( words[ 1 ] );
        if words[ 1 ] not in counts:
            counts[ words[ 1 ] ] = 1
        else:
            counts[ words[ 1] ] += 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:1]:
    print(val, key)
