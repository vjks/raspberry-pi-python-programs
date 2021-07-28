fhand = open('words.txt')
wordDictionary = dict()
count = 0

for line in fhand:    
    words = line.split()
    for word in words:
        count = count + 1
        print( word )
        wordDictionary[ word ] = count
        
print( wordDictionary )