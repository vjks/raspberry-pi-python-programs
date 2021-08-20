fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
    
counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len( words ) > 0 and words[ 0 ] == 'From':
        time = words[ 5 ].split(":") # The 5th word contains the time
        if time[ 0 ] not in counts: # The characters before the first color contain the hour
            counts[ time[ 0 ] ] = 1
        else:
            counts[ time[ 0 ] ] += 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((key, val))

lst.sort(reverse=False)

for key, val in lst[:]:
    print(key, val)