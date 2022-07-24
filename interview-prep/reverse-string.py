sentence = input("Enter a sentence:")
print("Sentence is: " + sentence)
sentenceArray = []
for character in sentence:
    sentenceArray.append(character)

for element in reversed(sentenceArray):
    print(element, end="")

print()

wordArray = sentence.split(" ")
for word in wordArray:
    newWord = []
    for character in word:
        newWord.append(character)
    for element in reversed(newWord):
        print(element, end="")
    print(" ", end="")

print()

for word in reversed(wordArray):
    print(word + " ", end="")
