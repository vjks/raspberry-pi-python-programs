fhand = open( 'mbox-short.txt' )
count = 0
for line in fhand:
    if line.startswith( 'From ' ):
        words = line.split()
        if words[0] == 'From':
            print( words[1] )
            count = count + 1
print( 'There are ', count, 'lines in the file with From as the first word' )
        
