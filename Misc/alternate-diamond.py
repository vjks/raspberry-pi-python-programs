input = int(input("Enter number of rows:" ))

for x in range(1, input + 1): # for numbers in range of 1 to input + 1
    space = " " * (input - x) # Spaces in the beginning are equal to the input - x
    result = ("*" + " ") * x  # Total number of asterix followed by space being added are equal to the current row number.
    print( space + result )

for x in reversed(range(1, input)):
    result = ("*" + " ") * x
    space = " " * (input  - x)
    print( space + result )