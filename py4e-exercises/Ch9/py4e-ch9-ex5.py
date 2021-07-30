fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
    
fromDomain = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len( words ) > 0 and words[ 0 ] == 'From':
        atpos = words[ 1 ].find( '@' ) # Find the position of the @ sign, the domain is after it.
        host = words[ 1 ][ atpos + 1 : ]  #From one character after @ sign to the end of the string.
        fromDomain[ host ] = fromDomain.get( host, 0 ) + 1
        
print( fromDomain )