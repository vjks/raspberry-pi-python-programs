letters = ['a', 'b', 'c', 'd', 'e']

def chop(argument):
    print(len(argument))
    del argument[0]
    del argument[ len(argument) - 1 ]
    return None
    
chop(letters)
print(letters)

def middle(argument):
    newList = argument[1: len(argument) - 1]
    return newList

afterFunctionCall = middle(letters)
print(letters)
print(afterFunctionCall)