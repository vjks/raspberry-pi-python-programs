import string
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
    
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate({ord(c): None for c in string.whitespace})
    line = line.lower()
    for character in line:
        if character not in counts:
            counts[character] = 1
        else:
            counts[character] += 1

print( counts )

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:]:
    print(val, key)