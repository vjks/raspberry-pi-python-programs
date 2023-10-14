import math

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    d = dict()
    
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    
    m = max(d, key=d.get)
    if m in d:
        d[m] = math.ceil(d[m] / 2)
    print(max(d.values()))