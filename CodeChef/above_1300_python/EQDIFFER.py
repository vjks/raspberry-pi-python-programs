import collections

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    d = dict()
    
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    
    high = 0
    high_key = 0
    for key, value in d.items():
        if value > high:
            high = value
            high_key = key
    
    total = 0
    for key, value in d.items():
        if key != high_key:
            total += value
    
    if n <= 2:
        print(0)
    elif total == n - 1:
        print(total - 1)
    else:
        print(total)