import math

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    # if k % n == 0:
    #     print(int(k / n))
    # else:
    #     i = 1
    #     while k % n != 0:
    #         k = k * i
    #         i += 1
    #     print(i - 1)
    
    if k % n == 0:
        print(1)
    else:
        lcm = math.lcm(n, k)
        print(int(lcm / k))