import math
t = int(input())

for _ in range(t):
    x, y, k = map(int, input().split())
    
    if k == 1:
        print(math.gcd(x, y) + min(x, y))
    else:
        print(2 * math.gcd(x, y))