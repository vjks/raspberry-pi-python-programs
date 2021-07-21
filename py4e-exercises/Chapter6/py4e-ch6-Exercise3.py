
def letterCounter(searchLetter, word):
    count = 0
    for letter in word:
        if letter == searchLetter:
            count = count + 1
    print("Total number of letter " + searchLetter + " in the word are: " + str(count))
letterCounter('a', "banana")