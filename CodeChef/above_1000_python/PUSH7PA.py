for _ in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    
    d = dict()
    
    for height in h:
        if height in d:
            d[height] += 1
        else:
            d[height] = 1
    
    total = 0
    for key, value in d.items():
        total = max(total, key + value - 1)
            
    print(total)