
import math #The math library is needed for calculating the square root and ceil functions

num = float(input("Enter a number:"))
sqrtOfNum = math.sqrt(num)

if ((math.ceil(sqrtOfNum) -  sqrtOfNum) == 0):
    print( str(num) + " is a perfect square")
else:
    print( str(num) + " is NOT a perfect square")
