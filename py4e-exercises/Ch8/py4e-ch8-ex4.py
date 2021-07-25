fhand = open('romeo.txt')
wordList = []

def checkList( checkWord ):
    for word in wordList:
        if word == checkWord:
            return True
    return False

for line in fhand:
    words = line.split()
    print('Debug:', words)
    if len(words) == 0 : continue
    for checkWord in words:        
        wordExists = checkList( checkWord )
        print( wordExists )
        if wordExists == False:
            wordList.append( checkWord )

wordList.sort()
print( wordList )