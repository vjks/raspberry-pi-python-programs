myString = "this is a string."
index = len(myString)
print("Length of the index is: " + str(index))
while index > 0:
    print(myString[index - 1], end='')
    index = index - 1