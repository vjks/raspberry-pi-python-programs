input = int(input("Enter number of rows:" ))

for x in range(1, input + 1):
    #print(x)
    result = ("*" * x ) + ("*" * (x - 1))
    space = " " * ( ( input + 1 ) - x )
    print( space + result )

for x in reversed(range(1, input)):
    #print(x)
    result = ("*" * x ) + ("*" * (x - 1))
    space = " " * ( ( input + 1 ) - x )
    print( space + result )