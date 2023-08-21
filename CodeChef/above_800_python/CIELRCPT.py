import math
t = int(input())

for _ in range(t):
    p = int(input())
    
    count = 0
    while(p != 0):
        #print(p)
        for i in reversed(range(12)):
            val = pow(2, i)
            if val <= p:
                count += 1
                p = p - val
                #print(val, i)
                break
    print(count)