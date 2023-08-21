
import math
t = int(input())

i = 0 
while(i < t):
    n = int(input())
    time = 0
    while n != 50:
        if n < 50:
            n += 2
            time += 1
        else:
            n -= 3
            time += 1
    print(time)
    i += 1
