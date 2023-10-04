import math
t = int(input())

for _ in range(t):
    n = int(input())
    factors = list()
    root = math.floor(math.sqrt(n))
    
    w = 1
    length = 0
    found = False
    for l in range(1, root + 1):
        if n % l == 0:
            x = int(n / l)
            if abs(l - x) < abs(n - w):
                w = x
                length = l
                found = True
    
    if not found:
        print(n - w)
    else:
        print(abs(length - w))