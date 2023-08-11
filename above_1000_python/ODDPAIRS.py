import math
t = int(input())

for _ in range(t):
    n = int(input())
    
    odds = math.ceil(n / 2)
    evens = n//2
    
    print(odds * evens * 2)