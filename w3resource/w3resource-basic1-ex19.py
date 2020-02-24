def stringAdder(enteredString):
    if len(enteredString) <= 2:
        return "String length is less than 2"
    elif enteredString[0] == 'I' and enteredString[1] == 's':
        return enteredString
    else:
        return "Is" + enteredString
    
print(stringAdder("hello"))
print(stringAdder("Isastring"))
print(stringAdder(""))

#test = "bababui"
#print(test[:3]) # Returns the first 3 characters of a string