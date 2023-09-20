import math
t = int(input())
for _ in range(t):
    l, v1, v2 = map(int, input().split())
    
    t1 = math.ceil(l / v1)
    t2 = math.ceil(l / v2)
    
    output = ""
    if t1 - t2 == 1:
        output = 0
    
    if t1 - t2 > 1:
        output = t1 - t2 - 1
    
    if t1 - t2 < 1:
        output = -1
    
    print(output)