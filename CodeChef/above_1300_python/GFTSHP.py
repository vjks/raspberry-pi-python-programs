# cook your dish here
import math

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    a.sort()
    total = 0
    discount = True
    for cost in a:
        if k <= 0:
            break
        
        if k - cost >= 0:
            k -= cost
            total += 1
            continue
            
        if discount and k - math.ceil(cost / 2) >= 0:
            k -= cost
            total += 1
            discount = False
    print(total)