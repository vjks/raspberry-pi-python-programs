import math

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 1:
        print(a[0])
    else:
        gcd = a[0]
        for _ in range(n - 1):
            gcd = math.gcd(gcd, a[_ + 1])
        print(gcd)