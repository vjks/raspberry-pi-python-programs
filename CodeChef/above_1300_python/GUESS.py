import math
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    odd = 0
    ways = 0
    
    # even from n and odd from m
    a = math.floor(n / 2) * math.ceil(m / 2)
    
    # odd from n and even from m
    b = math.ceil(n / 2) * math.floor(m / 2)
    
    y = n * m
    gcd = math.gcd(a + b, y)
    
    if gcd == 1:
        print(str(a + b) + '/' + str(y))
    else:
        x = int((a + b) / gcd)
        y = int(y / gcd)
        print(str(x) + '/' + str(y))