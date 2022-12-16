def alternate_capitals(input):
    i = 0
    modified_input = ""
    for character in input:
        #print( character )
        if i % 2 == 0:
            #print("{} is even".format( i ))
            modified_input = modified_input + character.upper()
            i = i + 1
            #print( i )
        else:
            modified_input = modified_input + character
            i = i + 1
    return modified_input

print( alternate_capitals("Hello, World!") )
print( alternate_capitals("hello") )
print( alternate_capitals("yo eli") )
print( alternate_capitals("hello???") )