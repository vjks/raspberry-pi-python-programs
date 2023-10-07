t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    
    d = dict()
    
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    count = 0
    for key, value in d.items():
        if value > 1:
            count += value - 1
    
    print(count)